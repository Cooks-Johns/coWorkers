import datetime
import math

import openpyxl

wb = openpyxl.Workbook()
ws = wb.active

# This will create a defualt workbook meaning there is always one
ws.title = "Items"
wb.iso_dates = True

date_and_time = datetime.datetime.now()


ws.append(['testing', 'this ', 'data', date_and_time.strftime("%X %m %H %I")])
ws.append(['testing2', 'this ', 'data', date_and_time.strftime("%a %d-%m-%Y")])
ws.append(['testing3', 'this ', 'data', date_and_time.strftime("%X %x")])
ws.append(['testing4', 'this ', 'data', date_and_time.strftime("%A %d-%m-%Y, %H:%M:%S")])
ws.append(['fin'])



wb.save('items.xlsx')




##### TEST OF DIFFERENT FORMATS
# dt = datetime.datetime.now()
#
# print(dt)
# print('\nDirectives\n--------------')
# print(dt.strftime('Weekday short version : %a'))
# print(dt.strftime('Weekday full version  : %A'))
# print(dt.strftime('Weekday as a number   : %w'))
# print(dt.strftime('Day of month          : %d'))
# print(dt.strftime('Month Name short ver  : %d'))
# print(dt.strftime('Month Name full ver   : %b'))
# print(dt.strftime('Month as a number     : %m'))
# print(dt.strftime('Year short version    : %y'))
# print(dt.strftime('Year full version     : %Y'))
# print(dt.strftime('Hour (00-23)          : %H'))
# print(dt.strftime('Hour (00-11)          : %I'))
# print(dt.strftime('AM/PM                 : %p'))
# print(dt.strftime('Minute                : %M'))
# print(dt.strftime('Second                : %S'))
#
#
# print('\nFormatted Date Strings\n--------------')
# print(dt.strftime('%a %d-%m-%Y'))
# print(dt.strftime('%a %d/%m/%Y'))
# print(dt.strftime('%a %d/%m/%y'))
# print(dt.strftime('%A %d-%m-%Y, %H:%M:%S'))
# print(dt.strftime('%X %x'))