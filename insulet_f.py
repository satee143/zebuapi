import os

import openpyxl

global wb,

os.chdir('/storage/emulated/0/Download')


def get_xlsx_region(xlsx_file, sheet, region):
    """ Return a rectangular region from the specified file.
    The data are returned as a list of rows, where each row contains a list 
    of cell values"""

    # 'data_only=True' tells openpyxl to return values instead of formulas
    # 'read_only=True' makes openpyxl much faster (fast enough that it 
    # doesn't hurt to open the file once for each region).
    wb = openpyxl.load_workbook(xlsx_file, data_only=True, read_only=True)

    reg = wb[sheet][region]

    return [[cell.value for cell in row] for row in reg]


# cache the lists of years and items
# get the first (only) row of the 'B1:F1' region
years = get_xlsx_region('comid.xlsx', 'Sheet1', 'B1:EE1')[0]
# get the first (only) column of the 'A2:A6' region
items = [r[0] for r in get_xlsx_region('comid.xlsx', 'Sheet1', 'A2:A554')]


def find_correct_cell(year, item):
    # find the indexes for 'COGS' and 2014
    year_col = chr(ord('B') + years.index(year))  # only works in A:Z range
    item_row = 2 + items.index(item)

    cell_reference = year_col + str(item_row)

    return cell_reference


rr = find_correct_cell(year=8478, item='8.1.1')
ws = wb['Sheet1']
ws[rr] = 'X'
wb.save('comid.xlsx')

# C3
