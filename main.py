from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from Objects.Register_page import RegisterPage
from Objects.Product_page import ProductPage
from Objects.Login_page import LoginPage


def main():
    # Configurar el driver manualmente
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    try:
        # --- Prueba manual de registro ---
        print("=== Probando RegisterPage ===")
        register = RegisterPage(driver)
        register.open()
        register.excute_register()
        print(f"URL actual: {driver.current_url}")

        # --- Prueba manual de login ---
        # print("=== Probando LoginPage ===")
        # login = LoginPage(driver)
        # login.open()
        # login.excute_login("aroba@pipra.com", "holamundo123")
        # print(f"URL actual: {driver.current_url}")

        # --- Prueba manual de producto ---
        # print("=== Probando ProductPage ===")
        # product = ProductPage(driver)
        # product.open()
        # product.add_to_car_product()
        # product.add_to_cart_with_options(1)

    except Exception as e:
        print(f"❌ Error: {e}")

    finally:
        driver.quit()  # siempre cierra el navegador


if __name__ == "__main__":
    main()