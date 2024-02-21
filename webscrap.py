# Database has been created, now I need to find something to scrap
import requests
import pandas
from bs4 import BeautifulSoup as bs
from database import add_many, show_all

# URL to scrape
url = "https://ca.finance.yahoo.com/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAB3us7daX04VBESr1vM9HG-djZ0D7IP1QYjoEenDpo39gcRmSH79fkPKA7-5MNoQRh-xbWuV92Svbe7ZGWHwlI1XYG22EI8dpKvAA7hMOp1dKSmCWTP1PUBuMHE_DHnof0eYvF4cFJ6dFunWbsWWq1_q4gNu1UUIb2I2gB3Amr7p"
page = requests.get(url)
web = bs(page.content, 'html.parser')

# Collecting titles and abouts
titles = []
abouts = []

all_stretch = web.find_all('li', attrs={'class': 'js-stream-content Pos(r)'})
for stretch in all_stretch:
    a_string = stretch.findAll('p', attrs={'class': "Fz(14px) Lh(19px) Fz(13px)--sm1024 Lh(17px)--sm1024 LineClamp(2,38px) LineClamp(2,34px)--sm1024 M(0)"})
    for p in a_string:
        abouts.append(p.text)

a_string = web.find_all('a', attrs={'class': 'js-content-viewer wafer-caas Fw(b) Fz(18px) Lh(23px) LineClamp(2,46px) Fz(17px)--sm1024 Lh(19px)--sm1024 LineClamp(2,38px)--sm1024 mega-item-header-link Td(n) C(#0078ff):h C(#000) LineClamp(2,46px) LineClamp(2,38px)--sm1024 not-isInStreamVideoEnabled'})
for string in a_string:
    titles.append('ca.finance.yahoo.com/' + string['href'])
# Adding data to the database
add_many(titles[:len(abouts)], abouts)