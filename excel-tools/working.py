from openpyxl import Workbook, load_workbook

wb = load_workbook('sa-voluteer.xlsx')
ws = wb.active  # worksheet

# When you are updating you must have the file closed inorder for this to work
ws["A2"].value = "Animal Care Services Department"
wb.save('sa-voluteer.xlsx')
