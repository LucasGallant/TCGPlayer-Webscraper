import scrapeCards
import scrapeWeb
import threading as th

def loopToPrintCardInfo(list):
    for link in list:
        scrapeCards.scrapeCardUrl(link)

# urls = scrapeWeb.scrapeFrontPage("https://www.tcgplayer.com/search/pokemon/product?productLineName=pokemon&page=1&view=grid")

# middleIndex = len(urls) // 2
# firstHalf = urls[:middleIndex]
# secondHalf = urls[middleIndex:]

# t1 = th.Thread(target=loopToPrintCardInfo, args=(firstHalf,))
# t2 = th.Thread(target=loopToPrintCardInfo, args=(secondHalf,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
scrapeCards.scrapeCardUrl("https://www.tcgplayer.com/product/684332/pokemon-me03-perfect-order-poke-pad-081-088?page=1&Language=English")