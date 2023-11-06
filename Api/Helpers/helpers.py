
import requests

BASE_URL = "https://reqres.in/api"


def create_user(data):
    response = requests.post(f"{BASE_URL}/users", json=data)
    return response


def get_user(user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    return response


def update_user(user_id, data):
    response = requests.put(f"{BASE_URL}/users/{user_id}", json=data)
    return response


def delete_user(user_id):
    response = requests.delete(f"{BASE_URL}/users/{user_id}")
    return response
