import pytest

@pytest.mark.run(order=1)
def test_opencart_homepage(driver):
    driver.get("http://localhost:8080/")
    assert "Your Store" in driver.title, "The page title does not indicate that we are on the Opencart homepage"