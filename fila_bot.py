from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Opciones para el controlador de Selenium
chrome_options = Options()
chrome_options.add_argument("--headless")  # Para ejecutar en modo sin cabeza

# Ruta al controlador de Selenium
chromedriver_path = '/path/al/controlador/chromedriver'  # Reemplaza con la ruta correcta

# Inicializar el controlador de Selenium
driver = webdriver.Chrome(chromedriver_path, options=chrome_options)

# URL del evento
url_evento = 'https://www.allaccess.com.ar/event/tan-bionica'

# Variable para controlar la redirección a la fila virtual
redireccion_fila_virtual = False

# Bucle para recargar la página cada 5 segundos hasta que ocurra la redirección
while not redireccion_fila_virtual:
    # Cargar la página
    driver.get(url_evento)
    print("Recargando la página...")

    # Comprobar si ha ocurrido la redirección a la fila virtual
    if driver.current_url != url_evento:
        redireccion_fila_virtual = True

    # Esperar 5 segundos antes de la siguiente recarga
    time.sleep(5)

# La redirección a la fila virtual ha ocurrido
print("Estás en la fila virtual. El navegador permanecerá abierto.")