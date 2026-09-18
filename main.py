import scrapeCards
import scrapeWeb
from concurrent.futures import ThreadPoolExecutor
import threading as th
import numpy as np

def loopToPrintCardInfo(list):
     for link in list:
          scrapeCards.scrapeCardUrl(link)

urls = scrapeWeb.scrapeFrontPage("https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&page=1&view=grid&ProductTypeName=Cards")


middleIndex = len(urls) // 2
firstHalf = urls[:middleIndex]
secondHalf = urls[middleIndex:]
t1 = th.Thread(target=loopToPrintCardInfo, args=(firstHalf,))
t2 = th.Thread(target=loopToPrintCardInfo, args=(secondHalf,))
t1.start()
t2.start()
t1.join()
t2.join()
#scrapeCards.scrapeCardUrl("https://www.tcgplayer.com/product/684332/pokemon-me03-perfect-order-poke-pad-081-088?page=1&Language=English")