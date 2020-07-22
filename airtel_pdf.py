### Importing modules ###
import os

import PyPDF2
import pandas as pd

from datetime import datetime

os.chdir('/storage/emulated/0/Download')

### Opening the PDF File as PdfFileObj ###
pdfFileObj = open('/storage/emulated/0/Download/DE1511756.pdf', 'rb')

### Reading the PDF file using PYPDF2 module as pdfReader Object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

### Creating list data types for storing the values in object
invoice, date, cgst, sgst, total, amountl = [], [], [], [], [], []

### Reading the Numpages in the PDF File
numpages = pdfReader.numPages

### Iterating through each Page to Find the values
for x in range(numpages):

    ### Going in to the each page
    pageObj = pdfReader.getPage(x)

    # Getting the Text from the Page
    page_text = pageObj.extractText()

    # Validating the Heading "Tax Invoice(Original for Recipient)" is avaliable in the Page
    if 'Tax Invoice(Original for Recipient)' in page_text:
        ### Finding the Invoice Number Text char Location index ###
        xy = page_text.find('Invoice Number:')
        # print(page_text[xy])

        ### Finding the Invoice Number last Digit Text char Location index ###
        xyz = page_text.find('GSTIN')
        # print(xyz)

        ###  Getting the Invoice Number by using index numbers
        invoice_number = page_text[xy + 15:xyz]
        # print(invoice_number)

        ### Finding the Invoice Number last Digit Text char Location index ###
        xy = page_text.find('Due Date:')
        # print(xy)
        ### Finding the Invoice Number last Digit Text char Location index ###
        xyz = page_text.find("Supplier's State Code:")
        # print(xyz)
        invoice_date = page_text[xy + 9:xyz]
        # print(invoice_date)

        xy = page_text.find('Total Amount')
        # print(xy)
        xyz = page_text.find('.', xy)
        amount = (page_text[xy + 12:xyz + 3])
        amt1 = float(amount.replace(',', ''))
        # print(float(amt1))
        # print(type(amt1))
        # print(amount)

        invoice.append(invoice_number)
        date.append(invoice_date)
        amountl.append(amt1)
        cgst_1 = (float(amt1)) * 9 / 100
        cgst_2 = round(cgst_1, 2)
        cgst.append(cgst_2)
        sgst_1 = (float(amt1)) * 9 / 100
        sgst_2 = round(cgst_1, 2)
        sgst.append(cgst_2)
        total2 = cgst_2 + sgst_2 + float(amt1)

        total.append(total2)

ex_data = pd.DataFrame(
    {
        'INVOICE_DATE': date,
        'INVOICE_NUMBER': invoice,
        'INVOICE_AMOUNT': amountl,

        'CGST': cgst,
        'SGST': sgst,
        'Total_amt': total

    }
)

# format date
date_object = datetime.strptime(invoice_date, "%d-%b-%Y")
month_year = str(date_object.strftime("%B-%Y")).upper()

# ex_data['sgst']=inv_amt*9,
# ex_data['total']=inv_amt+cgst+sgst9
ex_data.to_excel('/storage/emulated/0/Download/gst_file.xlsx', index=False, sheet_name=month_year)
print(ex_data)
