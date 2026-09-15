from selenium import webdriver 
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

nameXPATH = "/html/body/div[2]/div/div/section[2]/section/div[2]/div[2]/div[1]/h1"
priceXPATH = "/html/body/div[2]/div/div/section[2]/section/div[2]/div[2]/section[3]/div/div[1]/div[2]/section/div/table/tr[1]/td[2]"
avgDailySoldXPATH = "/html/body/div[2]/div/div/section[2]/section/div[2]/div[2]/section[3]/div/div[1]/div[3]/section/table/tr[2]/td[4]"

options = webdriver.FirefoxOptions()
options.add_argument("--headless")

def scrapeCardUrl(cardUrl):
    url = cardUrl

    driver = webdriver.Firefox(options=options) 
    driver.get(url)

    try: 
        name = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, nameXPATH)))
        price = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, priceXPATH)))
        avgDailySold = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, avgDailySoldXPATH)))
    except NoSuchElementException:
        print("Not Found")
        driver.quit()
    else:
        print("Found")
        print("Card Name: ", name.text)
        print("Card Price: ", price.text)
        print("Avg. Daily Sold: ", avgDailySold.text)
        driver.quit()