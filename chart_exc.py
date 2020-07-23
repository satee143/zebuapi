import os

os.chdir('/storage/emulated/0/ds')
print(os.getcwd())

from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference

workbook = Workbook()
sheet = workbook.active

# Let's create some sample sales data 
rows = [
    ["Product", "Online", "Store"],
    [1, 30, 45],
    [2, 40, 30],
    [3, 40, 25],
    [4, 50, 30],
    [5, 30, 25],
    [6, 25, 35],
    [7, 20, 40]]

for row in rows:
    sheet.append(row)
chart = BarChart()
data = Reference(worksheet=sheet,
                 min_row=1,
                 max_row=8,
                 min_col=2,
                 max_col=3)
chart.add_data(data, titles_from_data=True)
sheet.add_chart(chart, "E2")

workbook.save("chart.xlsx")
