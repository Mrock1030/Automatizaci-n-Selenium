import pytest
import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Navegador a usar: chrome o firefox"
    )

@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    print(f"\nIniciando navegador: {browser}")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        
        # options.add_argument("--headless")
        my_driver = webdriver.Chrome(options=options)  # ✅ Selenium 4 lo gestiona solo

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        my_driver = webdriver.Firefox(options=options)  # ✅ igual para firefox

    else:
        raise ValueError(f"Navegador no soportado: {browser}")

    yield my_driver
    my_driver.quit()