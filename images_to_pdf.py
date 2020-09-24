

from PIL import Image
import os
import PIL

# imagelist is the list with all image filenames
imagelist=[]

# write path of folder here
path='sample_data'
files = os.listdir(path)

# change basewidth to adjust size of image accordingly
basewidth=300 


for f in files:
  if f.endswith('jpg'):
    img_name=path+'/'+f
    img=Image.open(img_name)
    percent = (basewidth / float(img.size[0]))
    size = int((float(img.size[1]) * float(percent)))
    img = img.resize((basewidth, size), PIL.Image.ANTIALIAS)
    img_rgb=img.convert('RGB')
    imagelist.append(img_rgb)
  

imagelist

len(imagelist)

im1=imagelist[0]
imagelist=imagelist[1:]

len(imagelist)

im1.save(r'mypdf.pdf',save_all=True, append_images=imagelist)

