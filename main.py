import scrapeCards as sc    
import scrapeWeb as sw

#need to add error handleing
urls = sw.scrapeFrontPage("https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&page=1&view=grid&ProductTypeName=Cards")
if urls:
    sc.startScrape(urls)

