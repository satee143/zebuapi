import os

import qrcode

# example data
data = "https://www.thepythoncode.com"
# output file name
os.chdir('/storage/emulated/0/bluetooth')

filename = "site.png"
print(os.getcwd())
# generate qr code
img = qrcode.make(data)
# save img to a file
img.save(filename)
