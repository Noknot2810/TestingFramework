def test_google_search(driver):
    driver.get("https://google.com")
    assert driver.title == 'Google'
