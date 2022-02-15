import datetime
import openpyxl
import requests
from bs4 import BeautifulSoup

wb = openpyxl.Workbook()
ws = wb.active
page = requests.get("https://www.tripboba.com/article_quotes_123-top-dad-jokes-2021-to-make-you-the-funniest-guy-on-earth.html")  # Getting page HTML through request
soup = BeautifulSoup(page.content, 'html.parser')


# This will create a defualt workbook meaning there is always one
ws.title = "Items"
wb.iso_dates = True
date_and_time = datetime.datetime.now()

links = soup.select('ul li p')
first10 = links[:100]
for anchor in first10:
    ws.append([anchor.text, date_and_time])




wb.save('dadJokes.csv')

