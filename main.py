from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
import time

base_url = 'https://www.mercadolibre.com.ar/'

chrome_options = webdriver.ChromeOptions(); 
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging']);
driver = webdriver.Chrome(options=chrome_options);  

driver.get(base_url)
time.sleep(2)
driver.find_element(By.ID, 'newCookieDisclaimerButton').click()
time.sleep(3)

# Obtener h1, texto... meterlo en un json

div = driver.find_element(By.XPATH, '//div[@class="desktop__view-wrapper"]')
enlaces = div.find_elements(By.XPATH,'//a')

for enlace in enlaces:
    href = enlace.get_attribute('href')
    driver.get(enlace.get_at)
    products = driver.find_elements(By.XPATH, '//div[@class="ui-search-result__image"]')
    products_a = products.find_elements(By.XPATH,'//a')

    # Obtener h1, texto... meterlo en un json

    for product_a in products_a:
        driver.get(product_a.get_attribute('href'))
        # Obtener h1, descripcion,precio, img, meta description.... meterlo en un json
