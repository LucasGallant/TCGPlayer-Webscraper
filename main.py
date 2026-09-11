from selenium import webdriver 

options = webdriver.FirefoxOptions()
options.add_argument("--headless")

driver = webdriver.Firefox() 
driver.get("https://www.tcgplayer.com/")
print(driver)