import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.tripboba.com/article_quotes_123-top-dad-jokes-2021-to-make-you-the-funniest-guy-on-earth.html")  # Getting page HTML through request
soup = BeautifulSoup(page.content, 'html.parser')

links = soup.select('ul li p')
first10 = links[:100]
for anchor in first10:
    print(anchor.text)



# body > div.tb-content > div > div > div > div.col-lg-7.article-left-col > div:nth-child(2) ul li p