from openpyxl import Workbook, load_workbook

wb = load_workbook('sa-voluteer.xlsx')

# create a new sheet and then print out the sheets
wb.create_sheet("Test")
print(wb.sheetnames)