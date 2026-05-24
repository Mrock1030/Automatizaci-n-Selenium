from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from Objects.Base_page import BasePage


class ProductPage(BasePage):

    __url = 'https://demo.nopcommerce.com/desktops'

    locators = {
        "product_name": (By.XPATH, "//main[@id='main']/div[@class='master-column-wrapper']/section[@class='center-2']/div[@class='page category-page']/div[@class='page-body']/div[@class='products-container']/div[@class='products-wrapper']/div[@class='product-grid']/div[@class='item-grid']/div[@class='item-box'][1]/article[@class='product-item']/div[@class='details']/h2[@class='product-title']/a"),
        "add_to_car_button": (By.XPATH, "//main[@id='main']/div[@class='master-column-wrapper']/section[@class='center-2']/div[@class='page category-page']/div[@class='page-body']/div[@class='products-container']/div[@class='products-wrapper']/div[@class='product-grid']/div[@class='item-grid']/div[@class='item-box'][1]/article[@class='product-item']/div[@class='details']/div[@class='add-info']/div[@class='buttons']/button[@class='button-2 product-box-add-to-cart-button']"),
        "product_price": (By.XPATH, "//main[@id='main']/div[@class='master-column-wrapper']/section[@class='center-2']/div[@class='page category-page']/div[@class='page-body']/div[@class='products-container']/div[@class='products-wrapper']/div[@class='product-grid']/div[@class='item-grid']/div[@class='item-box'][1]/article[@class='product-item']/div[@class='details']/div[@class='add-info']/div[@class='prices']/span[@class='price actual-price']"),
        "count_producto": (By.XPATH, "//input[@id='product_enteredQuantity_1']"),
        "add_software": (By.XPATH, "//input[@id='product_attribute_5_12']"),
        "add_os": (By.XPATH, "//input[@id='product_attribute_4_9']"),
        "add_product": (By.XPATH, "//button[@id='add-to-cart-button-1']"),
        "add_disk": (By.XPATH, "//dd[@id='product_attribute_input_3']/ul[@class='option-list']/li[2]/label"),
        "select_ram": (By.XPATH, "//select[@id='product_attribute_2']"),
        "add_ok_product": (By.XPATH, "//div[@id='bar-notification']/div[@class='bar-notification success']/p[@class='content']"),
    }

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        self._open_url(self.__url)  

    def add_to_car_product(self):
        self._get_text(self.locators["product_name"])   
        self._get_text(self.locators["product_price"])
        self._click(self.locators["add_to_car_button"])
        return self.current_url  

    def add_to_cart_with_options(self, count: int = 3):
        self._click(self.locators["add_disk"])
        self._click(self.locators["add_os"])
        self._click(self.locators["add_software"])
        self._get_text(self.locators["select_ram"])
        self._type(self.locators["count_producto"], count)
        self._click(self.locators["add_product"])

    def validate_cart_addition(self):
        alert_message = self._wait_until_element_is_visible(self.locators["add_ok_product"], 5)
        return alert_message