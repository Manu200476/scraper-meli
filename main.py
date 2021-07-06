from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

base_url = 'https://www.mercadolibre.com.ar/'

chrome_options = webdriver.ChromeOptions(); 
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging']);
driver = webdriver.Chrome(options=chrome_options);  

try:
    wait = WebDriverWait(driver, 3000)
    driver.get(base_url)

    titles = driver.find_element(By.TAG_NAME, 'h3')
    print(titles)
except Exception as e:
    print(e)