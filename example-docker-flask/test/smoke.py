#!/usr/bin/env python

import os
import pytest
import requests
from urllib.parse import urljoin


def test_version():
    r = requests.get(urljoin(os.environ['HOST'], '/about'))
    assert r.status_code == requests.codes.ok
    assert r.json()['version'] == os.environ['VERSION']
