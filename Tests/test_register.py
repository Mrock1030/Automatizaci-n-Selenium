import time
import re
from Objects.Register_page import RegisterPage

def test_register(driver):
    """
    Test: Registrar usuario con los datos predeterminados
    Verifica que el formulario se complete y se registre exitosamente
    """
    register_page = RegisterPage(driver)
    print("Abriendo página de registro...")
    register_page.open()
    time.sleep(3)
    
    print("Relleno formulario y registro...")
    register_page.excute_register()
    # 4. Esperar el resultado del registro
    time.sleep(2)
    # 5. Verificar el resultado (Buscamos mensajes clave de éxito)
    success_message = driver.page_source
    
    # Buscamos mensajes típicos de éxito en la demo (depende del título del formulario)
    # Buscamos 'Producto añadido' o 'Usuario registrado' o mensajes similares
    success_pattern = r"(producto añadido|usuario registrado|registro exitoso)"
    assert re.search(success_pattern, success_message, re.IGNORECASE), \
        f"El registro no fue procesado correctamente. " \
        f"Mensaje de éxito encontrado: '{success_message}'"
    
    print("¡Test PASSED! El registro fue exitoso.")
    

def test_register_negative_user(driver):
    """
    Test: EL USUARIO NO INGRESA NOMBRE DE USUARIO
    """
    register_page = RegisterPage(driver)
    print("Abriendo página de registro...")
    register_page.open()
    time.sleep(3)
    
    print("Relleno formulario y registro...")
    register_page.excute_register('','123@pipratonge.com','tongeo_pipra')
    # 4. Esperar el resultado del registro
    time.sleep(2)
    # 5. Verificar el resultado (Buscamos mensajes clave de éxito)
    success_message = driver.page_source
    

    success_faild= r"(First name is required)"
    assert re.search(success_faild, success_message, re.IGNORECASE), \
        f"El registro no fue procesado correctamente. " \
        f"Mensaje de éxito encontrado: '{success_message}'"

def test_register_negative_password(driver):
    "" """
    Test: EL USUARIO NO INGRESA cONTRASEÑA
    """
    register_page = RegisterPage(driver)
    print("Abriendo página de registro...")
    register_page.open()
    time.sleep(3)
    
    print("Relleno formulario y registro...")
    register_page.excute_register('Camilo','1234@pipratonge.com','')
    # 4. Esperar el resultado del registro
    time.sleep(2)
    # 5. Verificar el resultado (Buscamos mensajes clave de éxito)
    success_message = driver.page_source
    
    # Buscamos mensajes típicos de éxito en la demo (depende del título del formulario)
    # Buscamos 'Producto añadido' o 'Usuario registrado' o mensajes similares
    success_faild= r"(Password is required)"
    assert re.search(success_faild, success_message, re.IGNORECASE), \
        f"El registro no fue procesado correctamente. " \
        f"Mensaje de éxito encontrado: '{success_message}'"

    
    