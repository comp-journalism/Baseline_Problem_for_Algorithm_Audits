# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 21:22:26 2017

@author: jenniferstark

This script checks the images are not too large for Micrsofts API, which has a
limit of 1kb to 4MB

"""

import sys, glob
from PIL import Image

def check_img_size(candidate, file_dir):

    body = ""

#    file_dir = './' + candidate + "_unique_images/"
#    big_dir = 'big_images/'
#    small_dir = 'small_images/'
        
    #load image
    for image_filename in glob.glob(file_dir + '*.jpg'):
        #print(image_filename)

        with open(image_filename, 'rb') as f:
            #print(f)
            body = f.read()

            if sys.getsizeof(body) > 3500000:  # checking the image is just below the upped limit, just to be safe (3.4MB)
                print('True', image_filename)

                basewidth = 600

                img = Image.open(image_filename)
                wpercent = (basewidth / float(img.size[0]))
                hsize = int((float(img.size[1]) * float(wpercent)))
                img = img.resize((basewidth, hsize), Image.ANTIALIAS)

                try:
                    output_file = image_filename.split('/')[2].strip('.jpg')
                except IndexError:
                    print(image_filename)
                    output_file = image_filename.split('/')[1].strip('.jpg')

                img.save(output_file + '_resized.jpg')
                print("image resized")

check_img_size('hillary_clinton','hillary_clinton_image_universe/' )
