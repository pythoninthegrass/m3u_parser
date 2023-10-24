# m3u_prsr

Parses an M3U playlist file into a list of track objects.

Builds on the excellent work of [dvndrsn's](https://github.com/dvndrsn) [M3uParser](https://github.com/dvndrsn/M3uParser).

## Setup
* Minimum requirements
  * [Python 3.11](https://www.python.org/downloads/)
* Dev dependencies
  * [editorconfig](https://editorconfig.org/)

## Quickstart
```bash
# setup virtual environment
python -m venv .venv
source .venv/bin/activate

# install
python -m pip install m3u-prsr

# run
m3u-prsr ./tests/fixtures/test.m3u
```

## Development
* Setup environment
    ```bash
    # install dependencies
    poetry install

    # activate virtual environment
    poetry shell
    ```
* Run script
    ```
    # run against the example m3u file
    λ app/main.py tests/fixtures/test.m3u
    Minus The Bear - Burying Luck.mp3 (0s)
    Minus The Bear - Ice Monster.mp3 (0s)
    Minus The Bear - Knights.mp3 (0s)
    Minus The Bear - White Mystery.mp3 (0s)
    Minus The Bear - Dr. l'Ling.mp3 (0s)
    Minus The Bear - Part 2.mp3 (0s)
    Minus The Bear - Throwin' Shapes.mp3 (0s)
    Minus The Bear - When We Escape.mp3 (0s)
    Minus The Bear - Double Vision Quest.mp3 (0s)
    Minus The Bear - Lotus.mp3 (0s)
    Parsed 10 tracks from ../tests/fixtures/test.m3u
    ```
* Testing
    ```bash
    # generate tests
    cd app/
    hypothesis write main.parsem3u > ../tests/test_m3u_parser.py

    # run specific test
    pytest -k test_m3u_parser

    # install from testpypi
    pip install -i https://test.pypi.org/simple/ m3u-prsr
    ```

## TODO
* [Issues](https://github.com/pythoninthegrass/m3u_prsr/issues)
* Button up error handling for internal field separators on m3u track names
* Tests
* CI/CD

## Further Reading
[The M3U File Format « The Matthew Nielsen Web Experience](https://web.archive.org/web/20180809050707/http://n4k3d.com/the-m3u-file-format)

[Repositories | Documentation | Poetry - Python dependency management and packaging made easy](https://python-poetry.org/docs/repositories/)

[How to Build and Publish Python Packages With Poetry](https://www.freecodecamp.org/news/how-to-build-and-publish-python-packages-with-poetry/)

[Packaging your Python Project](https://skerritt.blog/packaging-your-python-project/)

[python - Use poetry to create binary distributable with pyinstaller on package? - Stack Overflow](https://stackoverflow.com/a/77181745/15454191)

[`poetry publish` raises HTTP 403 · Issue #6320 · python-poetry/poetry](https://github.com/python-poetry/poetry/issues/6320#issuecomment-1234036608)

[Tips and Tricks - Test and publish your Python packages to PyPI with poetry and GitHub Actions | TestDriven.io](https://testdriven.io/tips/810f9bb5-c9df-479d-baa4-290c7e0779f1/)
