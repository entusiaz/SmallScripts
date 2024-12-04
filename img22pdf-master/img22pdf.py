from flask import Flask

# app = Flask(__name__)

#--- LONG VERSION ---#
import os
import urllib.request
from PIL import Image
import img2pdf


# image_source = "https://www.baseone.co/_next/static/media/whyAfrica.29a92d2f.svg"
# image_source = "image1.jpg"

# if image_source == LINK
if image_source[:5] == "https":
    image_retrieved = urllib.request.urlretrieve(image_source, "image_retrieved.png")
    image = Image.open(image_retrieved[0])  
    # print(image)
    pdf = img2pdf.convert(image.filename)
    file = open("./pdf_file.pdf", "wb")
    file.write(pdf)

# if image_source == PATH:
elif os.path.exists(image_source):
    image = Image.open(image_source)
    pdf = img2pdf.convert(image.filename)
    file = open("./pdf_file.pdf", "wb")
    file.write(pdf)

else:
    print("...Kindly provide a clear image source...")

print("Finished!....")


#--- SHORT VERSION ---#
# with open("pdf_file.pdf","wb") as f:
#     f.write(img2pdf.convert('image1.jpg'))
