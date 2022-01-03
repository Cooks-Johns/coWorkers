import datetime
import math

import openpyxl
from openpyxl import Workbook, load_workbook

wb = openpyxl.Workbook()
ws = wb.active

# This will create a defualt workbook meaning there is always one
ws.title = "Items"
wb.iso_dates = True

date_and_time = datetime.datetime.now()


ws.append(['testing', 'this ', 'data', date_and_time])
ws.append(['testing2', 'this ', 'data', date_and_time])
ws.append(['testing3', 'this ', 'data', date_and_time])
ws.append(['testing4', 'this ', 'data', date_and_time])
ws.append(['fin'])



wb.save('items.xlsx')

