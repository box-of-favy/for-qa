# test_url.py
import requests
import pytest

def test_url_status(url):
    """Проверка, что указанный URL возвращает статус код 200."""
    response = requests.get(url)
    assert response.status_code == 200, f"URL {url} returned status code {response.status_code}"
