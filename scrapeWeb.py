from httpcore import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#CSS worked better than XPATH for some reason
cardUrlCSS = "html body div#app.app-container div div.marketplace section.marketplace__content section.unified-search section section.search-layout-hfb section section.search-results div.search-result div.search-result__content div.search-result__product div.product-card div.product-card__content a"
sortButtonXPATH = "/html/body/div[3]/div/div/section[2]/section/section/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div/div/div[1]"
bestSellingXPATH = "/html/body/div[3]/div/div/section[2]/section/section/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div/div/div[2]/ul/li[2]/span"

options = webdriver.FirefoxOptions()
options.add_argument("--headless")


def getHrefs(driver):
    # one JS call, so nothing can go stale halfway through
    return driver.execute_script(
        "return Array.from(document.querySelectorAll(arguments[0])).map(a => a.href);",
        cardUrlCSS,
    )


def scrapeFrontPage(url):
    driver = webdriver.Firefox()
    try:
        driver.get(url)
        wait = WebDriverWait(driver, 20)

        # wait for the first batch of cards, remember what it looked like
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, cardUrlCSS)))
        before = getHrefs(driver)

        wait.until(EC.element_to_be_clickable((By.XPATH, sortButtonXPATH))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, bestSellingXPATH))).click()

        # wait until the list has changed from the unsorted one
        wait.until(lambda d: getHrefs(d) != before)

        # then wait until it stops changing (two identical reads in a row)
        def stable(d):
            first = getHrefs(d)
            d.implicitly_wait(0)
            return first and first == getHrefs(d) and first

        urls = wait.until(stable)
        print("Found")
        return list(dict.fromkeys(urls))   # dedupe, keep order

    except TimeoutException:
        print("Not Found")
        return None
    finally:
        driver.quit()