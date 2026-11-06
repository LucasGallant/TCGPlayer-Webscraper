import scrapeCards
import scrapeWeb

#need to add error handleing
urls = scrapeWeb.scrapeFrontPage("https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&page=1&view=grid&ProductTypeName=Cards")
scrapeCards.startScrape(urls)