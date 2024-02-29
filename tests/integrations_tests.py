import pytest
from po2.src.structure import User, Group
from po2.src.logic import Logic

@pytest.fixture
def logic():
    return Logic()

def test_integration_add_and_get_user(logic):
    user = {"firstName": "Eduard", "lastName": "Muntianov", "birthYear": 2007, "group": Group("user")}
    logic.add_user(user)
    added_user = logic.get_user(1)
    expected_user = {"id": 1, "firstName": "Eduard", "lastName": "Muntianov", "birthYear": 2007, "group": Group("user")}
    assert added_user == expected_user

def test_integration_update_and_get_user(logic):
    user = {"firstName": "Eduard", "lastName": "Muntianov", "birthYear": 2007, "group": "user"}
    logic.add_user(user)
    updated_user = {"firstName": "Anna", "lastName": "Muntianova", "birthYear": 2007, "group": Group("user")}
    logic.update_user(1, updated_user)
    updated_user = logic.get_user(1)
    expected_user = {"id": 1, "firstName": "Anna", "lastName": "Muntianova", "birthYear": 2007, "group": Group("user")}
    assert updated_user == expected_user

def test_integration_delete_user(logic):
    user = {"firstName": "Eduard", "lastName": "Muntianov", "birthYear": 2007, "group": "user"}
    logic.add_user(user)
    logic.delete_user(1)
    deleted_user = logic.get_user(1)
    assert deleted_user is None