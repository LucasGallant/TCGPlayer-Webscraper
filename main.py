import scrapeCards
import scrapeWeb
import threading as th
from concurrent.futures import ThreadPoolExecutor, as_completed

def loopToPrintCardInfo(list):
     for link in list:
          scrapeCards.scrapeCardUrl(link)

#need to add error handleing
urls = scrapeWeb.scrapeFrontPage("https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&page=1&view=grid&ProductTypeName=Cards")

middleIndex = len(urls) // 2
firstHalf = urls[:middleIndex]
secondHalf = urls[middleIndex:]

with ThreadPoolExecutor(max_workers=3) as executor:
    # Submit tasks to the executor (returns Future objects)
    futures = [executor.submit(scrapeCards.scrapeCardUrl(urls[0]), i) for i in range(5)]
# t1 = th.Thread(target=loopToPrintCardInfo, args=(firstHalf,))
# t2 = th.Thread(target=loopToPrintCardInfo, args=(secondHalf,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()