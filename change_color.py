from PIL import Image
import os
os.chdir('/storage/emulated/0/Download')

image = Image.open('image.jpg')

image.show()

image_data = image.load()

height,width = image.size
print(height,width)

for loop1 in range(height):
    for loop2 in range(width):
        r,g,b = image_data[loop1,loop2]
        image_data[loop1,loop2] = 0,0,b

image.save('changed.jpeg')