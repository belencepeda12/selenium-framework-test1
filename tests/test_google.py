from selenium import webdriver
from selenium.webdriver.common.by import By


def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


def test_google_title():
    driver = setup_driver()

    driver.get("https://www.google.com")

    assert driver.title == "Google"

    driver.quit()


def test_google_search_box_exists():
    driver = setup_driver()

    driver.get("https://www.google.com")

    search_box = driver.find_element(By.NAME, "q")

    assert search_box.is_displayed()

    driver.quit()


def test_google_page_url():
    driver = setup_driver()

    driver.get("https://www.google.com")

    assert "google.com" in driver.current_url

    driver.quit()


def test_google_logo_exists():
    driver = setup_driver()

    driver.get("https://www.google.com")

    logo = driver.find_element(By.CSS_SELECTOR, "img[alt='Google']")

    assert logo.is_displayed()

    driver.quit()


def test_google_search():
    driver = setup_driver()

    driver.get("https://www.google.com")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium WebDriver")
    search_box.submit()

    assert "Selenium WebDriver" in driver.title

    driver.quit()