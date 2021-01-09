#!/usr/bin/env python

import os
import pytest
import requests
from urllib.parse import urljoin


@pytest.fixture(scope="module", autouse=True)
def test_env():
    missing = ['HOST', 'VERSION'] - os.environ.keys()
    if missing:
        print('Missing environment variables: ' + ','.join(missing))
        assert False


def test_prediction():
    r = requests.get(os.environ['HOST'])
    assert r.status_code == requests.codes.ok
    assert 'connotation' in r.json()
    assert 'response' in r.json()


def test_version():
    r = requests.get(urljoin(os.environ['HOST'], '/about'))
    assert r.status_code == requests.codes.ok
    assert r.json()['version'] == os.environ['VERSION']


def test_health():
    r = requests.get(urljoin(os.environ['HOST'], 'ping/data'))
    assert r.status_code == requests.codes.ok
    assert r.content == b'PONG data'
