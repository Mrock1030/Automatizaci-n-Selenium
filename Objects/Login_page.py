from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from . import Base_page

class LoginPage(BasePage):
    __url ='https://demo.nopcommerce.com/login?returnUrl=%2F'
    __email_field=(By.XPATH,"//input[@id='Email']")
    __password_field =(By.XPATH,"//input[@id='Password']")
    __submit_button=(By.XPATH,"//main[@id='main']/div[@class='master-column-wrapper']/section[@class='center-1']/div[@class='page login-page']/div[@class='page-body']/div[@class='customer-blocks']/div[@class='returning-wrapper fieldset']/form/div[@class='buttons']/button[@class='button-1 login-button']")
    __forgot_password =(By.XPATH,"//main[@id='main']/div[@class='master-column-wrapper']/section[@class='center-1']/div[@class='page login-page']/div[@class='page-body']/div[@class='customer-blocks']/div[@class='returning-wrapper fieldset']/form/div[@class='form-fields']/div[@class='inputs reversed']/span[@class='forgot-password']/a")
    __remenber_me =(By.XPATH,"//main[@id='main']/div[@class='master-column-wrapper']/section[@class='center-1']/div[@class='page login-page']/div[@class='page-body']/div[@class='customer-blocks']/div[@class='returning-wrapper fieldset']/form/div[@class='form-fields']/div[@class='inputs reversed']/label")
    __see_password=(By.XPATH,"//main[@id='main']/div[@class='master-column-wrapper']/section[@class='center-1']/div[@class='page login-page']/div[@class='page-body']/div[@class='customer-blocks']/div[@class='returning-wrapper fieldset']/form/div[@class='form-fields']/div[@class='inputs'][2]/div[@class='login-password']/span[@class='password-eye']")
                  
    def __init__(self, driver:WebDriver):
        super().__init__(driver)
    
    def open (self):
        self.open_url(self.__url)
    
    def excute_login(self,email:str, password:str):
        self._type(self.__email_field,email)
        self._type(self.__password_field,password)
        self._click(self.__see_password)
        try:
            self._click(self.__submit_button)
        except Exception as Error:
            try:
                self._click(self.__submit_button)
            except:
                raise Exception("No se pudo encontrar el botón de LOG IN")
    def excute_forgot_password(self):
        self._click(self.__forgot_password)
        
    def excute_remenber_me(self):
        self._click(self.__remenber_me)
        
    
        
    
        
    