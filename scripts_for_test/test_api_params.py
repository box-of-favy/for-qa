import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    assert len(response.json()) > 0  # Проверяем, что список постов не пустой

@pytest.mark.parametrize("post_id", [1, 100])
def test_get_post(post_id):
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200
    assert response.json()['id'] == post_id  # Проверяем, что ID поста соответствует запрошенному

@pytest.mark.parametrize("user_id", [1, 2])
def test_get_posts_by_user(user_id):
    response = requests.get(f"{BASE_URL}/posts", params={'userId': user_id})
    assert response.status_code == 200
    posts = response.json()
    assert all(post['userId'] == user_id for post in posts)  # Проверяем, что все посты принадлежат указанному пользователю

def test_create_post():
    new_post = {
        "title": 'foo',
        "body": 'bar',
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    assert response.status_code == 201
    json_resp = response.json()
    assert json_resp["title"] == new_post["title"]
    assert json_resp["body"] == new_post["body"]
    assert json_resp["userId"] == new_post["userId"]

def test_delete_post():
    post_id = 1
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200
