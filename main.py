import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

base_url = 'https://www.mercadolibre.com.ar/categorias'

chrome_options = webdriver.ChromeOptions(); 
driver = webdriver.Chrome(options=chrome_options);  

driver.get(base_url)
time.sleep(2)

links = driver.find_elements(By.XPATH, '//li[@class="categories__item"]/a')
link_href = []

for link in links:
    href = link.get_attribute('href')
    link_href.append(href)

for href in link_href:
    time.sleep(3)
    driver.get(href)

    while True:

        products = driver.find_elements(By.XPATH, '//div[@class="ui-search-result__image"]/a')
        products_href = []
        for product in products:
            href = product.get_attribute("href")
            products_href.append(href)

        for href in products_href:
            driver.get(href)
            time.sleep(2)
            name = driver.find_element(By.XPATH, '//h1')
            price = driver.find_element(By.XPATH, '//span[@class="price-tag-fraction"]')
            num_reviews = driver.find_element(By.XPATH, '//span[@class="ui-pdp-review__amount"]')
            reviews = driver.find_elements(By.XPATH, '//di[@class="ui-pdp-reviews__comments__review-comment"]')
            description = driver.find_element(By.XPATH, '//p[@class="ui-pdp-description__content"]')
            characteristics = driver.find_element(By.XPATH, '//table[@class="andes-table"]')
        
        try:
            next_page = driver.find_element(By.PARTIAL_LINK_TEXT  , 'Siguiente')
            driver.get(next_page.get_attribute('href'))
        except Exception as e:
            break
    
driver.quit()