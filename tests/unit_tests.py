import pytest

from po2.src.api import validate_user
from po2.src.structure import Group
from po2.src.logic import Logic

@pytest.fixture
def logic():
    return Logic()

def test_get_users(logic):
    assert logic.get_users() == []

def test_add_user(logic):
    user = {"firstName": "Eduard", "lastName": "Muntianov", "birthYear": 2007, "group": "user"}
    logic.add_user(user)
    expected_user = {"id": 1, "firstName": "Eduard", "lastName": "Muntianov", "birthYear": 2007, "group": Group("user")}
    assert logic.get_users() == [expected_user]

def test_get_user(logic):
    user = {"firstName": "Eduard", "lastName": "Muntianov", "birthYear": 2007, "group": Group("user")}
    logic.add_user(user)
    user['id'] = 1
    assert logic.get_user(1) == user

def test_update_user(logic):
    user = {"firstName": "Eduard", "lastName": "Muntianov", "birthYear": 2007, "group": "user"}
    updated_user = {"firstName": "Anna", "lastName": "Muntianova", "birthYear": 2007, "group": Group("user")}
    logic.add_user(user)
    logic.update_user(1, updated_user)
    updated_user['id'] = 1
    assert logic.get_user(1) == updated_user

def test_delete_user(logic):
    user = {"firstName": "Eduard", "lastName": "Muntianov", "birthYear": 2007, "group": "user"}
    logic.add_user(user)
    logic.delete_user(0)
    assert logic.get_user(0) is None

def test_validate_user(logic):
    user = {"firstName": "Eduard", "lastName": "Muntianov", "birthYear": 2007, "group": "user"}
    assert validate_user(user)
    invalid_user = {"firstName": "Eduard", "lastName": "Muntianov", "birthYear": 2007, "group": "userr"}
    assert not validate_user(invalid_user)