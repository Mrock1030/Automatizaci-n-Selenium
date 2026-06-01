from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from faker import Faker


class BasePage:
    
    faker = Faker()
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _wait_until_element_is_visible(self, locator: tuple, timeout: int = 10, menssage: str = None):
        wait = WebDriverWait(self._driver, timeout)
        return wait.until(ec.visibility_of_element_located(locator))

    def _wait_for_url_contains(self, partial_url: str, timeout: int = 10):
        WebDriverWait(self._driver, timeout).until(
        ec.url_contains(partial_url))
        
    def _wait_navegator(self,timeout:int=50):
        wait = WebDriverWait(self._driver, timeout)
        
    def _click_with_scroll(self, locator: tuple, timeout: int = 10):
        element = self._wait_until_element_is_visible(locator, timeout)
        self._driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        
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
    
    def _skip_cloudflare(self):
        try:
            print("Verificando si aparece Cloudflare...")
            iframes = self._driver.find_elements(By.TAG_NAME, "iframe")
            if not iframes:
                print("Cloudflare no apareció.")
                return
            self._driver.switch_to.frame(iframes[0])

            checkbox = WebDriverWait(self._driver, 30).until(
                ec.element_to_be_clickable(
                    (By.XPATH,'//*[@id="challenge-stage"]/div/label/input')) )
            checkbox.click()
            print("Cloudflare resuelto correctamente.")
            # Volver al contenido principal
            self._driver.switch_to.default_content()
        except Exception as e:
            print(f"No se pudo resolver Cloudflare: {e}")
            self._driver.switch_to.default_content()
                    
    @property
    def current_url(self) -> str:
        return self._driver.current_url