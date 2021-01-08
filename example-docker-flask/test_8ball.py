import pytest

from flask import json
from app import app, response_pool, version
from pytest_mock import mocker

@pytest.fixture
def client():
    return app.test_client()

def test_health_check(client):
    """Validate the health check responds."""

    rv = client.get('/ping')
    assert rv.status_code == 200
    assert b'PONG' in rv.data

def test_health_check_with_data(client):
    """Validate the health check echoes data back."""

    data = 'foobar'

    rv = client.get('/ping/' + data)
    expected_reply = 'PONG ' + data

    assert rv.status_code == 200
    assert str.encode(expected_reply) in rv.data

def test_prediction(client, mocker):
    """Validate the 8-ball response."""

    chosen = response_pool()[3]
    choice = mocker.patch('app.choice')
    choice.return_value = chosen

    rv = client.get('/')
    data = json.loads(rv.data)

    choice.assert_called_once_with(response_pool())

    assert data['connotation'] == chosen['connotation']
    assert data['response'] == chosen['response']

def test_about(client):
    """Validate the about endpoint."""

    rv = client.get('/about')
    data = json.loads(rv.data)

    assert data['version'] == version

def test_largest_prime_factor(client):
    rv = client.get('/largest-prime-factor/35')
    data = json.loads(rv.data)

    assert data['prime-factor'] == 7