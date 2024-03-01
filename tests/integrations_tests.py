import pytest
from po2.src.api import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_integration_add_and_get_user(client):
    user = {"firstName": "Eduard", "lastName": "Muntianov", "birthYear": 2007, "group": "user"}
    response = client.post('/users', json=user)
    assert response.status_code == 201
    response = client.get('/users/1')
    assert response.status_code == 200
    assert response.get_json() == {"id": 1, "firstName": "Eduard", "lastName": "Muntianov", "birthYear": 2007, "group": "user"}

def test_integration_update_and_get_user(client):
    user = {"firstName": "Eduard", "lastName": "Muntianov", "birthYear": 2007, "group": "user"}
    updated_user = {"firstName": "Anna", "lastName": "Muntianova", "birthYear": 2007, "group": "user"}
    client.post('/users', json=user)
    client.patch('/users/1', json=updated_user)
    response = client.get('/users/1')
    assert response.status_code == 200
    assert response.get_json() == {"id": 1, "firstName": "Anna", "lastName": "Muntianova", "birthYear": 2007, "group": "user"}

def test_integration_delete_user(client):
    user = {"firstName": "Eduard", "lastName": "Muntianov", "birthYear": 2007, "group": "user"}
    client.post('/users', json=user)
    response = client.delete('/users/1')
    assert response.status_code == 200
    response = client.get('/users/1')
    assert response.status_code == 404