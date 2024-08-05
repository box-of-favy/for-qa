import json
import pprint
import requests

r = requests.get('https://dog.ceo/api/breeds/list/all')
parsed_data = r.json()

def test_1():
    assert r.status_code == 200

def test_2():
    assert r.headers['content-type'] is not None

def test_3():
    assert r.encoding.lower() == 'utf-8'

def test_4():
    assert "otterhound" in parsed_data['message']
    assert parsed_data['message']["otterhound"] == []
def test_5():
    assert "message" in parsed_data
    assert isinstance(parsed_data["message"], dict)


def test_url_status(param_url):
    """Проверка, что указанный URL возвращает статус код 200."""
    response = requests.get(param_url)
    assert response.status_code == 200, f"URL {param_url} вернул статус код {response.status_code}"

def test_breed_list(param_url):
    """Проверка, что ответ от URL содержит ключ 'message'."""
    response = requests.get(param_url)
    data = response.json()
    assert response.status_code == 200, f"URL {param_url} вернул статус код {response.status_code}"
    assert "message" in data, f"Key 'message' not found in response from {param_url}"

# Пример использования фикстуры url
def test_specific_url(url):
    """Проверка, что указанный URL из опции возвращает статус код 200."""
    response = requests.get(url)
    assert response.status_code == 200, f"URL {url} вернул статус код {response.status_code}"
