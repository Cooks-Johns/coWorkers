from openpyxl import Workbook, load_workbook

wb = load_workbook('sa-voluteer.xlsx')
ws = wb.active  # worksheet
print(ws['A2'].value) # to get the value of a cell


d