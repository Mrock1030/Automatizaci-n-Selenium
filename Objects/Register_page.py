from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from Objects.Base_page import BasePage


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

                  
    def __init__(self, driver:WebDriver):
        super().__init__(driver)
    
    def open (self):
        self.open_url(self.__url)
    
    def excute_register(self,user:str='juanca',lastname:str='Martinez',company:str='Prueba'
                        ,email:str='aroba@pipra.com',password:str='holamundo123'):
        try:
            self._type(self.__username,user)
            self._type(self.__last_username,lastname)
            self._type(self.__email,email)
            ##agregamos el company name
            self._type(self.__company_name,company)
            ##agregamos la contraseña
            self._type(self.__user_password,password)
            self._type(self.__confirm_password,password)
        except:
        #Encontramos el sexo del usuario
            try:
                self._find(self.__gender_sex)
                self._click(self.__gender_sex)
            except Exception as Error:
                try:   
                    self._click(self.__submit_button_register)
                except Exception as Error:
                    try:
                        self._click(self.__submit_button_register)
                    except:
                        raise Exception("No se pudo encontrar el botón de REGISTER")
                
            
        
    
        
    