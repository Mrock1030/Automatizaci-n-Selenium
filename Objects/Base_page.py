from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException


class BasePage:

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _wait_until_element_is_visible(self, locator: tuple, timeout: int = 10, menssage: str = None):
        wait = WebDriverWait(self._driver, timeout)
        return wait.until(ec.visibility_of_element_located(locator))

    def _type(self, locator: tuple, text: str, timeout: int = 10):
        self._wait_until_element_is_visible(locator, timeout)
        self._find(locator).clear()
        self._find(locator).send_keys(str(text))

    def _click(self, locator: tuple, timeout: int = 10):
        self._wait_until_element_is_visible(locator, timeout)
        self._find(locator).click()

    def _get_text(self, locator: tuple, timeout: int = 10) -> str:
        self._wait_until_element_is_visible(locator, timeout)
        return self._find(locator).text

    def is_displayed(self, locator: tuple) -> bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def _open_url(self, url: str):
        self._driver.get(url)

    @property
    def current_url(self) -> str:
        return self._driver.current_url