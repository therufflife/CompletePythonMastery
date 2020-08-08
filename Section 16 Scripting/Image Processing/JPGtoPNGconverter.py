import sys
import os
from PIL import Image

#grab first and second arguments
image_folder = sys.argv[1]
output_folder = sys.argv[2]

#check if new folder exists, if not create
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#loop through Pokedex, convert to png, save to new folder
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    # print(clean_name)
    img.save(f'{output_folder}{clean_name}', 'png')
    print('all done!')