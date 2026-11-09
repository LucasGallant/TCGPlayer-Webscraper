import cardDatabase
from selenium import webdriver 
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

nameXPATH = "/html/body/div[2]/div/div/section[2]/section/div[2]/div[2]/div[1]/h1"
priceXPATH = "/html/body/div[2]/div/div/section[2]/section/div[2]/div[2]/section[3]/div/div[1]/div[2]/section/div/table/tr[1]/td[2]"
avgDailySoldXPATH = "/html/body/div[2]/div/div/section[2]/section/div[2]/div[2]/section[3]/div/div[1]/div[3]/section/table/tr[2]/td[4]"
setNameXPATH = "/html/body/div[2]/div/div/section[2]/section/div[2]/div[2]/div[1]/div/div/div/a/span"

#so it doesnt open a visable window
options = webdriver.FirefoxOptions()
options.add_argument("--headless")

def scrapeCardUrl(url, driver):

    driver.get(url)

    try:
        # have to use WebDriverWait or else it will return null
        name = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, nameXPATH)))
        price = driver.find_element(By.XPATH, priceXPATH)
        avgDailySold = driver.find_element(By.XPATH, avgDailySoldXPATH)
        setName = driver.find_element(By.XPATH, setNameXPATH)

    # exception if no element was found for any of them
    # NEEDS TO BE CHANGED TO CHECK INDIVIDUAL
    except NoSuchElementException:
        print("Didnt find for: " + name)
    else:
        if not (name == None or price == None or avgDailySold == None or setName == None):
            cardDatabase.databaseInsert(name.text, price.text, avgDailySold.text, setName.text, url)
        
        else:
            print("Null Value")

def startScrape(urls):
    driver = webdriver.Firefox(options=options)
    for url in urls:
        scrapeCardUrl(url, driver)
        print("Finished for URL: " + url)
    driver.quit()