import pytest
from po2.src import api
from po2.src.structure import User
from po2.src.logic import Logic

@pytest.fixture
def logic():
    return Logic()

def test_get_users(logic):
    assert logic.get_users() == []

def test_add_user(logic):
    user = {"firstName": "John", "lastName": "Doe", "birthYear": 1990, "group": "user"}
    logic.add_user(user)
    expected_user = {"id": 1, "firstName": "John", "lastName": "Doe", "birthYear": 1990, "group": User.Group.user}
    assert logic.get_users() == [expected_user]

def test_get_user(logic):
    user = {"firstName": "John", "lastName": "Doe", "birthYear": 1990, "group": "user"}
    logic.add_user(user)
    assert logic.get_user(0) == user

def test_update_user(logic):
    user = {"firstName": "John", "lastName": "Doe", "birthYear": 1990, "group": "user"}
    updated_user = {"firstName": "Jane", "lastName": "Doe", "birthYear": 1990, "group": "user"}
    logic.add_user(user)
    logic.update_user(0, updated_user)
    assert logic.get_user(0) == updated_user

def test_delete_user(logic):
    user = {"firstName": "John", "lastName": "Doe", "birthYear": 1990, "group": "user"}
    logic.add_user(user)
    logic.delete_user(0)
    assert logic.get_user(0) is None

def test_validate_user(logic):
    user = {"firstName": "John", "lastName": "Doe", "birthYear": 1990, "group": "user"}
    assert logic.validate_user(user)
    invalid_user = {"firstName": "John", "lastName": "Doe", "birthYear": "1990", "group": "user"}
    assert not logic.validate_user(invalid_user)