from selenium import webdriver 
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading
import json

nameXPATH = "/html/body/div[2]/div/div/section[2]/section/div[2]/div[2]/div[1]/h1"
priceXPATH = "/html/body/div[2]/div/div/section[2]/section/div[2]/div[2]/section[3]/div/div[1]/div[2]/section/div/table/tr[1]/td[2]"
avgDailySoldXPATH = "/html/body/div[2]/div/div/section[2]/section/div[2]/div[2]/section[3]/div/div[1]/div[3]/section/table/tr[2]/td[4]"
setNameXPATH = "/html/body/div[2]/div/div/section[2]/section/div[2]/div[2]/div[1]/div/div/div/a/span"

#so it doesnt open a visable window
options = webdriver.FirefoxOptions()
options.add_argument("--headless")

def threadName(driver):
    name = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, nameXPATH)))
    return name

def threadPrice(driver):
    price = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, priceXPATH)))
    return price

def scrapeCardUrl(url):
    driver = webdriver.Firefox(options=options) 
    driver.get(url)

    try: 
        # have to use WebDriverWait or else it will return null
        # name = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, nameXPATH)))
        # price = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, priceXPATH)))
        # avgDailySold = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, avgDailySoldXPATH)))
        # setName = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, setNameXPATH)))
        t1 = threading.Thread(target=threadName, args=(driver,))
        t2 = threading.Thread(target=threadPrice, args=(driver,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    # exception if no element was found for any of them
    #NEEDS TO BE CHANGED TO CHECK INDIVIDUAL
    except NoSuchElementException:
        print("Not Found")
        driver.quit()
    else:
        # jFile = {
        #     "name": name.text,
        #     "cardInfo": {
        #                 "price": price.text,
        #                 "avgDailySold": avgDailySold.text
        #                 }
        # }
        # json_str = json.dumps(jFile, indent=3)
        # with open("sample.json", "w") as f:         
        #     f.write(json_str)
        # if not (name == None or price == None or avgDailySold == None or setName == None):
        #     print("--------------------------------------------------------------------------------------")
        #     print("Card Name: ", name.text)
        #     print("Card Price: ", price.text)
        #     print("Avg. Daily Sold: ", avgDailySold.text)
        #     print("Set: ", setName.text)
        #     print("Url: ", url)
        # else:
        #     print("Null Value")
        print(t1)
        print(t2)

        driver.quit()