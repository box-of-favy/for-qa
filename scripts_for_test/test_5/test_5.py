# test_opencart.py
def test_opencart_homepage(browser, base_url):
    browser.get(base_url)
    assert "Your Store" in browser.title, "The page title does not indicate that we are on the Opencart homepage"
