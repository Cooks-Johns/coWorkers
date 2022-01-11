import requests
from bs4 import BeautifulSoup

page = requests.get("https://covid19.sanantonio.gov/What-YOU-Can-Do/Testing#TestingLocation")  # Getting page HTML through request
soup = BeautifulSoup(page.content, 'html.parser')

links = soup.select('tbody tr td')
first10 = links[:1000]
for anchor in first10:
    print(anchor.text)





#tablesaw-7761 > tbody tr:nth-child(1) td:nth-child(5)