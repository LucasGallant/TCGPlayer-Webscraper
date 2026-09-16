import scrapeCards
import scrapeWeb

urls = scrapeWeb.scrapeFrontPage("https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&page=1&view=grid")
for link in urls:
    scrapeCards.scrapeCardUrl(link)  