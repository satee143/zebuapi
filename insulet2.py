import os

import openpyxl

global wb
os.chdir('/storage/emulated/0/Download')

wb = openpyxl.load_workbook('comid.xlsx')
reg = wb['Sheet1']['B1:EE1']
result1 = [[cell.value for cell in row] for row in reg][0]
reg = wb['Sheet1']['A2:A554']
result = [[cell.value for cell in row] for row in reg]
items = [r[0] for r in result]
year_col = chr(ord('B') + result1.index(8476))  # only works in A:Z range
item_row = 2 + items.index('1.2')
cell_reference = year_col + str(item_row)
print(cell_reference)
ws = wb['Sheet1']
ws[cell_reference] = 'XYZ'
wb.save('comid.xlsx')
