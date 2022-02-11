from tests.const import (
    TEST_MINT,
    TEST_PUBKEY,
    TEST_PRIVKEY
)

def test_load_state(client):
    data = {}
    response = client.post("/tank/load", json=data)
    assert response.status_code == 200


def test_save_state(client):
    data = {}
    response = client.post("/tank/save", json=data)
    assert response.status_code == 200
