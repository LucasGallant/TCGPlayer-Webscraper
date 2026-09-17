import scrapeCards
import scrapeWeb

urls = scrapeWeb.scrapeFrontPage("https://www.tcgplayer.com/search/magic/product?productLineName=magic&page=1&view=grid")
print(urls)