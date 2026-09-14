from selenium import webdriver 
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

url = "https://www.tcgplayer.com/product/702350/yugioh-chaos-origins-black-chaos?page=1&Language=English"

options = webdriver.FirefoxOptions()
options.add_argument("--headless")

driver = webdriver.Firefox(options=options) 
driver.get(url)

try: 
    element = driver.find_elements(By.CSS_SELECTOR, 'h1.product-details__name')
    driver.quit()
except NoSuchElementException:
    print("Not Found")
else:
    print("Found")
    print(element.text)