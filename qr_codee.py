
import os,qrdecode

import qrcode
# example data
data = "https://www.onlinesbi.com"
# output file name
os.chdir('/storage/emulated/0/bluetooth')

filename="dusa.png"
print(os.getcwd())
# generate qr code
img = qrcode.make(data)
# save img to a file
img.save(filename)
#
x=qrdecode.decode(filename)
print(x)

# read the QRCODE image
#img = cv2.imread("site.png")