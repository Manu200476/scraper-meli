import time
from selenium import webdriver
from selenium.webdriver.common.by import By

base_url = 'https://www.mercadolibre.com.ar/categorias'

chrome_options = webdriver.ChromeOptions(); 
driver = webdriver.Chrome(options=chrome_options);  

driver.get(base_url)
time.sleep(2)

links = driver.find_elements(By.XPATH, '//li[@class="categories__item"]/a')

print('URL: ' + driver.current_url)

for link in links:
    time.sleep(3)
    href = link.get_attribute('href')
    driver.get(href)
    products = driver.find_elements(By.XPATH, '//div[@class="ui-search-result__image"]/a')
    products_href = []

    for product in products:
        href = product.get_attribute("href")
        products_href.append(href)

    for href in products_href:
        time.sleep(4)
        driver.get(href)
        time.sleep(2)
        name = driver.find_element(By.XPATH, '//h1')
        price = driver.find_element(By.XPATH, '//span[@class="price-tag-fraction"]')
        num_reviews = driver.find_element(By.XPATH, '//span[@class="ui-pdp-review__amount"]')
        reviews = driver.find_elements(By.XPATH, '//di[@class="ui-pdp-reviews__comments__review-comment"]')
        description = driver.find_element(By.XPATH, '//p[@class="ui-pdp-description__content"]')
        characteristics = driver.find_element(By.XPATH, '//table[@class="andes-table"]')

        p = {
            'name': name,
            'price': price,
            'num_reviews': num_reviews,
            'reviews': reviews,
            'description': description,
            'characteristics': characteristics
        }
        

    # pagination_button.click()

