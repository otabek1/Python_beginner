import sys
import os

from PIL import Image
folder = sys.argv[1]
newf = sys.argv[2]
if not (os.path.exists(newf)):
    os.makedirs(newf)

for filename in os.listdir(folder):
    im = Image.open(f"{folder}{filename}")
    clean_name = os.path.splitext(filename)
    png = im.save(f"{newf} {clean_name[0]}.png", "png")
    # print(image_list)
