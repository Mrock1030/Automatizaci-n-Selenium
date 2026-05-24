import pytest
import os
import sys
import time
import base64
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

# Asegura que page_objects sea importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Navegador para ejecutar los tests: chrome o firefox"
    )


@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    print(f"\nIniciando navegador: {browser}")

    if browser == "chrome":
        my_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == "firefox":
        my_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise TypeError(f"Navegador no soportado: '{browser}'. Usa 'chrome' o 'firefox'.")

    my_driver.maximize_window()
    yield my_driver

    print(f"\nCerrando navegador: {browser}")
    my_driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    driver = item.funcargs.get("driver", None)

    if report.when != "call" or driver is None:
        return

    cwd = os.path.dirname(os.path.abspath(__file__))
    report_dir = os.path.join(cwd, "reports")
    assets_dir = os.path.join(report_dir, "assets")
    os.makedirs(assets_dir, exist_ok=True)

    timestamp = time.strftime("%Y%m%d-%H%M%S")
    status = "failed" if report.failed else "passed"
    filename = f"{item.name}_{status}_{timestamp}.png"
    abs_path = os.path.join(assets_dir, filename)

    try:
        saved = driver.save_screenshot(abs_path)
    except Exception as e:
        print(f"[screenshot] Error: {e}")
        saved = False

    if saved:
        try:
            from pytest_html import extras
            with open(abs_path, "rb") as f:
                b64 = base64.b64encode(f.read()).decode("utf-8")
            extra_img = extras.image(b64, mime_type="image/png", extension="png")
            if hasattr(report, "extra"):
                report.extra.append(extra_img)
            else:
                report.extra = [extra_img]
            outcome.force_result(report)
        except Exception as e:
            print(f"[screenshot] Error adjuntando al reporte: {e}")