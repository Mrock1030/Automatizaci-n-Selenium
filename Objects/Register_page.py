from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from Objects.Base_page import BasePage
from faker import Faker

class RegisterPage(BasePage):
    __url='https://demo.nopcommerce.com/register?returnUrl=%2F'
    __username = (By.XPATH, "//input[@id='FirstName']")
    __last_username = (By.XPATH, "//input[@id='LastName']")
    __email = (By.XPATH, "//input[@id='Email']")
    __company_name = (By.XPATH, "//input[@id='Company']")
    __user_password = (By.XPATH, "//input[@id='Password']")
    __confirm_password = (By.XPATH, "//input[@id='ConfirmPassword']")
    __submit_button_register = (By.XPATH, "//button[@id='register-button']")
    __gender_sex=(By.XPATH,"//input[@id='gender-male']")
    fake = Faker() 
                  
    def __init__(self, driver:WebDriver):
        super().__init__(driver)
    
    def open (self):
        self._open_url(self.__url)

    def excute_register(self, 
                        user=fake.first_name(), 
                        lastname=fake.last_name(), 
                        company: str = 'Prueba',
                        email=fake.email(), 
                        password=fake.password()):    
        self._type(self.__username,user)
        self._type(self.__last_username,lastname)
        self._type(self.__email,email)
        self._type(self.__company_name,company)
        self._type(self.__user_password,password)
        self._type(self.__confirm_password,password)
        self._find(self.__gender_sex)
        self._click(self.__gender_sex)
        self._click(self.__submit_button_register)
        self._wait_navegator()
          
        
    
        
    