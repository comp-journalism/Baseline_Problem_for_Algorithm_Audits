# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 14:37:16 2016

@author: jenniferstark


from https://realpython.com/blog/python/fingerprinting-images-for-near-duplicate-detection/

Script assigns difference hash to each image.
Puts hash in a shelf along with all images that have that hash (ie. all repeats of that image)
"""

from PIL import Image
import imagehash
import argparse
import shelve
import glob

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument('-d', '--dataset', required = True,
                help = 'path to imput dataset of images')
ap.add_argument('-s', '--shelve', required = True,
                help = 'output shelve database')
args = ap.parse_args()

# open the shelve database
db = shelve.open(args.shelve, writeback = True)

# loop over the image dataset
for imagePath in glob.glob(args.dataset + '/*.jpg'):
    # load the image and compute the difference in hash
    image = Image.open(imagePath)
    h = str(imagehash.dhash(image))
    print(h)

    # extract the filename from the path and update the database using the hash
    # as the key and the filename append to the list of values

    filename = imagePath[imagePath.rfind('/') + 1:]
    db[h] = db.get(h, []) + [filename]
    #print(db[h])
# close the shelf database
db.close()

# python index.py --dataset ./clinton --shelve db.shelve
