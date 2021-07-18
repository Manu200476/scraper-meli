from selenium.webdriver.common.by import By

class SEOInfo:
    def __init__(self, driver):
        self.driver = driver

    # Meta Datos
    def meta_description(self):
        meta_description = self.driver.find_elements(By.XPATH, '//meta[@name="description"]/@content')
        print('Meta Description: ' + meta_description)

    def title(self):
        title = self.driver.find_elements(By.XPATH, '//title')
        print(title)

    # Headings
    def extract_h1(self):
        h1 = self.driver.find_elements(By.XPATH, '//h1')
        print('Numero de H1: '+ len(h1))
    
    def extract_h2(self):
        h2 = self.driver.find_elements(By.XPATH, '//h2')
        print('Numero de H2: '+ len(h2))

    def extract_h3(self):
        h3 = self.driver.find_elements(By.XPATH, '//h3')
        print('Numero de H3: '+ len(h3))
    
    # Content

    def content(self):
        content = self.driver.find_elements(By.CSS_SELECTOR, 'body.p')
        print(content)

    # Links

    def rel_links(self):
        enlaces = self.driver.find_elements(By.XPATH, '//a')
        follow = []
        nofollow = []

        for enlace in enlaces:
            attribute_rel = enlace.get_attribute('rel')
            if attribute_rel == 'follow': 
                follow.append(enlace)
            else:
                nofollow.append(enlace)

        print('Enlaces follow: ' + len(follow))
        print('Enlaces nofollow: ' + len(nofollow))

    def linktype(self):
        enlaces = self.driver.find_elements(By.XPATH, '//a')
        interno = []
        externo = []
        for enlace in enlaces:
            href = enlace.get_attribute('href')
            decision = 'mercadolibre.com.ar' in href
            if decision:
                interno.append(enlace)
            else:
                externo.append(enlace)

        print('Enlace Interno: ' + len(interno))
        print('Enlace externo: ' + len(externo))