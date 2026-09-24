from selenium import webdriver 
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#CSS worked better than XPATH for some reason
cardUrlCSS = "html body div#app.app-container div div.marketplace section.marketplace__content section.unified-search section section.search-layout-hfb section section.search-results div.search-result div.search-result__content div.search-result__product div.product-card div.product-card__content a"
sortButtonXPATH = "/html/body/div[2]/div/div/section[2]/section/section/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div"
bestSellingXPATH = "/html/body/div[2]/div/div/section[2]/section/section/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div/div/div[2]/ul/li[2]/span"

#so it doesnt open a visable window
options = webdriver.FirefoxOptions()
options.add_argument("--headless")

def scrapeFrontPage(url):
    driver = webdriver.Firefox(options=options) 
    driver.get(url)

    try: 
        WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, sortButtonXPATH)))
        sortButton = driver.find_element(By.XPATH, sortButtonXPATH)
        sortButton.click()
        bestSelling = driver.find_element(By.XPATH, bestSellingXPATH)
        bestSelling.click()

        # have to use WebDriverWait or else it will return null
        links = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, cardUrlCSS)))
        urls = []
        for link in links:
            url1 = link.get_attribute("href")

            if url1:
                urls.append(url1)

    # exception if no element was found
    except NoSuchElementException:
        print("Not Found")
        driver.quit()
    else:
        print("Found")
        driver.quit()
        return urls