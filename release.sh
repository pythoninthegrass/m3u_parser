#!/usr/bin/env bash

# shellcheck disable=SC2046,SC2086,SC2162

cat << 'DESCRIPTION' >/dev/null
release.sh

Reads .env for PyPi token and publishes to PyPi or TestPyPi

USAGE
	./release.sh

NOTES
	- Requires poetry
	- Requires .env file in project root
	- Requires pyproject.toml in project root
	- POETRY_PYPI_TOKEN_PYPI is the PyPi token (prod)
	- POETRY_TEST_PYPI_TOKEN_PYPI is the TestPyPi token (dev)
	- REPO can be either "dev" (TestPyPi) or "prod" (PyPi)
DESCRIPTION

GIT_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"
SCRIPT_DIR=$(dirname "$(readlink -f "$0")")

# get the root directory
if [ -n "$GIT_ROOT" ]; then
	TLD="$(git rev-parse --show-toplevel)"
else
	TLD="${SCRIPT_DIR}"
fi

ENV_FILE="${TLD}/.env"

# source .env file skipping commented lines
if [ -f "${ENV_FILE}" ]; then
	export $(grep -v '^#' ${ENV_FILE} | xargs)
else
	echo ".env file not found in ${TLD}"
	exit 1
fi

# verify pyproject.toml is present
if [ ! -f "${TLD}/pyproject.toml" ]; then
	echo "pyproject.toml not found in ${TLD}"
	exit 1
fi

# get pypi token
if [[ -z "$POETRY_PYPI_TOKEN_PYPI" ]]; then
    read -s -p "Please enter your PyPi auth token: " POETRY_PYPI_TOKEN_PYPI
fi

# add testpypi repo if test pypi token is present (optional)
if [[ -n "$POETRY_TEST_PYPI_TOKEN_PYPI" ]]; then
    poetry config repositories.testpypi "https://test.pypi.org/legacy/"
fi

# get repo
if [[ -z "$REPO" ]]; then
	read -p "Please enter the repo to publish to (dev/prod): " REPO
fi

# build (if older than n minutes)
if find ./dist -mmin -30 | grep -q dist; then
	echo "Skipping build"
else
	echo "Building..."
	poetry build
fi

# publish
case "$REPO" in
    dev)
        echo "Publishing to TestPyPi..."
        poetry publish -u "__token__" -p "$POETRY_TEST_PYPI_TOKEN_PYPI" -r "testpypi"
        ;;
    prod)
        echo "Publishing to PyPi..."
        poetry publish -u "__token__" -p "$POETRY_PYPI_TOKEN_PYPI"
        ;;
    "")
        echo "No repo specified"
        exit 1
        ;;
    *)
        echo "Invalid repo specified"
        exit 1
        ;;
esac

exit 0
