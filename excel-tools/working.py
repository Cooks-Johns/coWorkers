import datetime
import openpyxl

wb = openpyxl.Workbook()
ws = wb.active

# This will create a defualt workbook meaning there is always one
ws.title = "Items"

date_and_time = datetime.datetime.now()

# todo figure out why the date and time is showing up as ##########
ws.append(['testing', 'this ', 'data', date_and_time])
ws.append(['testing2', 'this ', 'data', date_and_time])
ws.append(['testing3', 'this ', 'data', date_and_time])
ws.append(['testing4', 'this ', 'data', date_and_time])
ws.append(['fin'])



wb.save('items.xlsx')

