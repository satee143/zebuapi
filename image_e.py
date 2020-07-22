import os

from PIL import Image
from PIL.ExifTags import TAGS

os.chdir('/storage/emulated/0/ds')

# path to the image or video
imagename = "image.jpg"

# read the image data using PIL
image = Image.open(imagename)

exifdata = image.getexif()
print(exifdata)
# iterating over all EXIF data fields
for tag_id in exifdata:
    # get the tag name, instead of human unreadable tag id
    tag = TAGS.get(tag_id, tag_id)
    # print(tag)
    data = exifdata.get(tag_id)
    # decode bytes 
    if isinstance(data, bytes):
        data = data.decode()
    print(f"{tag:30}: {data}")

image = image.resize((4000, 3000), Image.ANTIALIAS)
image.save('resize.jpg')
