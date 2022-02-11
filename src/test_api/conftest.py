import os
import pytest
from api.utils import TestConfig

from .const import TEST_MINT, TEST_PUBKEY, TEST_PRIVKEY

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = create_app(config_object=TestConfig())

    yield app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


class AuthActions:
    def __init__(self, client):
        self._client = client

    def login(self, mint=TEST_MINT, pub=TEST_PUBKEY, priv=TEST_PRIVKEY):
        data = {
            "player": {
                "pub": pub,
                "priv": priv,
                "mint": mint
            }
        }
        response = self._client.post("/load_state", json=data)

        assert response.status_code == 200
        return response

    def logout(self):
        """No logout server-side; user must prove themselves with cookies"""


@pytest.fixture
def auth(client):
    return AuthActions(client)
