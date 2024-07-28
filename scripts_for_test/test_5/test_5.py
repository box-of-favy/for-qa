# test_opencart.py
import pytest

@pytest.mark.parametrize("browser_name", ["chrome", "firefox", "ie"])
def test_opencart_homepage(browser_name, browser, base_url):
    browser.get(base_url)
    assert "Your Store" in browser.title, "The page title does not indicate that we are on the Opencart homepage"

@pytest.fixture
def browser_name(request):
    return request.param