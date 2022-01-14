import openpyxl
import requests
from bs4 import BeautifulSoup

wb = openpyxl.Workbook()
ws = wb.active
page = requests.get("https://www.tripboba.com/article_quotes_123-top-dad-jokes-2021-to-make-you-the-funniest-guy-on-earth.html")  # Getting page HTML through request
soup = BeautifulSoup(page.content, 'html.parser')


# This will create a defualt workbook meaning there is always one
ws.title = "dadJokes"
wb.iso_dates = True


ws.append([("..")])


links = soup.select('ul li p')
first133 = links[:133]

for anchor in first133:
    ws.append([anchor.text])




wb.save('dadJokes.xlsx')

