import pytest

from Api.Helpers.helpers import create_user, get_user, update_user, delete_user


def test_create_user():
    user_data = {
        "name": "John Doe",
        "job": "Tester"
    }
    response = create_user(user_data)
    assert response.status_code == 201


def test_get_user():
    user_id = 1
    response = get_user(user_id)
    assert response.status_code == 200


def test_update_user():
    user_id = 1
    user_data = {
        "name": "Updated Name",
        "job": "Updated Job"
    }
    response = update_user(user_id, user_data)
    assert response.status_code == 200


def test_delete_user():
    user_id = 1
    response = delete_user(user_id)
    assert response.status_code == 204


if __name__ == "__main__":
    pytest.main()
