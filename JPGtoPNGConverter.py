import sys
import os
from PIL import Image

#grab the first and second argument
inp = sys.argv[1]
outp = sys.argv[2]
#check if folder exists, if not create it
if not os.path.exists(outp):
    os.mkdir(outp)
#loop through folder, convert to png
for file in os.listdir(inp):
    img = Image.open(f'.\{inp}\{file}')
    if file.endswith('.jpg'):
        file = file.replace('.jpg', '')
# save to new folder
        img.save(f'{outp}\{file}.png', 'png')
        print(f'{file} converted to PNG!')
        continue
    else:
        continue
print('All JPG\'s converted!')
