from PIL import Image
from glob import glob
from os.path import splitext

jpglist = glob( "/Users/xieyanduo/Desktop/pythonBird/photo/*.*" )

for p in jpglist:
    print(splitext(p)[0])
    text = splitext(p)[0] + '.jpg'
    im = Image.open(p)
    im.save(text)
