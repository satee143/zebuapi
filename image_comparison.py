import os
os.chdir('/storage/emulated/0/Download')

from PIL import Image ,ImageChops
img1=Image.open("1.jpg")
img2=Image.open("2.jpg")
diff=ImageChops.difference(img1,img2)
diff.save('3.jpg')
if diff.getbbox():
	diff.show()