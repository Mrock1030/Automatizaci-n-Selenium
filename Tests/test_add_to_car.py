import time
import re
from ..Objects import Product_page

def test_add_car(driver):
    """
    Test: Registrar un producto al carrito
    Verifica que se añada al carrito un producto.
    """
    add_car= ProductPage(driver)
    print("Abriendo página de registro...")
    add_car.open()
    
    print("Relleno formulario y registro...")
    actual_url= add_car.add_to_car_product()
    print(f"URl obtenida depsues de la acción:{actual_url}")
    
    expected_url="https://demo.nopcommerce.com/build-your-own-computer"
    
    print(f"Validando url...")
    assert actual_url == expected_url,f"Error La redirección fallo. se esperaba {expected_url}, pero se obtuvo {actual_url}"
    
    add_car.add_to_cart_with_options(1)
    add_car.validate_cart_addition()
    
    try:
        assert add_car.validate_cart_addition().is_displayed()
        print("✅ Éxito: La alerta de añadido al carrito fue encontrada.")

    except Exception as e:
        # Si el tiempo se agota o no se encuentra el elemento, lanzamos un error
        print(f"❌ Error en la validación: No se encontró la alerta. Error: {e}")
        raise AssertionError("Fallo en la validación de la alerta del carrito.")

  
    
    
    
