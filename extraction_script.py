
import os
import sys
import uuid

import matplotlib.image as mpimg
import numpy as np

def extract_images(image, spriteWidth_x, spriteWidth_y):
    imgShape = image.shape;
    images = {}

    for y in range(0,imgShape[1],spriteWidth_y):
        for x in range(0,imgShape[0],spriteWidth_x):
            try:
                subImage = image[y:y+spriteWidth_y,x:x+spriteWidth_x,:]

                name = str(uuid.uuid4().hex) + '.png'

                images[name] = {}
                images[name]['img'] = subImage

            except Exception as e:
                print(e)
    return images

if __name__ == '__main__':

    if len(sys.argv) != 5:
        print('{} sourceFile destinationFolder spriteX spriteY\n'.format(sys.argv[0]))
        exit()
    else:
        sourceFile = sys.argv[1]
        destinationFolder = sys.argv[2]
        spriteX = int(sys.argv[3])
        spriteY = int(sys.argv[4])

    img = mpimg.imread(sourceFile)

    images = extract_images(img, spriteX, spriteY)

    for imgName in images.keys():
        try:
            mpimg.imsave(os.path.join(destinationFolder, imgName), images[imgName]['img'])
        except:
            print(e)