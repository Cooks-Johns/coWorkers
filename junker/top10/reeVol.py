import requests
from bs4 import BeautifulSoup
from bs4.diagnose import diagnose


page = requests.get("https://covid19.sanantonio.gov/What-YOU-Can-Do/Testing#TestingLocation")  # Getting page HTML through request
soup = BeautifulSoup(page.content, 'html.parser')

links = soup.select('tbody')
first10 = links[:1000]
for anchor in first10:
    print(anchor.text)


with open("bad.html") as fp:
    data = fp.read()
diagnose(data)

#event-list > div.items > a:nth-child(1) > div > div > div.details > div.details-text > div.title > div
#event-list > div.items > a:nth-child(1) > div > div > div.details > div.details-text > div.title > div group-title group-link