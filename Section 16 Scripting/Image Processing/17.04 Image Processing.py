# Image Processing
from PIL import Image, ImageFilter

img = Image.open('./astro.jpg')
print(img.size)

img.thumbnail((400,400))         # sets image max to 400
img.save('thumb.jpg')
print(img.size)             # sets max to 400 and resizes sides