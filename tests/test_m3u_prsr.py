#!/usr/bin/env python3

import pytest
import sys
from hypothesis import given, HealthCheck, settings, strategies as st
from pathlib import Path

# get top level directory
tld = Path(__file__).parent.parent.resolve()

# import app/m3u_parser.py
sys.path.append(str(tld / 'app'))
import app.main as main

# suppress healthcheck warnings
settings.register_profile("dev", suppress_health_check=list(HealthCheck))
settings.load_profile("dev")


@pytest.fixture
def m3u_file():
    return f"{tld}/tests/fixtures/test.m3u"


@given(verbose=st.booleans())
def test_parsem3u(m3u_file, verbose):
    main.parsem3u(infile=m3u_file, verbose=verbose)
