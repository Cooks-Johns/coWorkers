import datetime
import openpyxl

wb = openpyxl.Workbook()
ws = wb.active

# This will create a defualt workbook meaning there is always one
ws.title = "Items"
date_and_time = datetime.datetime.now()



wb.save('items.xlsx')

