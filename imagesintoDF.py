# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 19:20:13 2016

@author: jenniferstark

This script is meant to:

* Each image has a hash which is stored in the shelf
* Using that hash, we can identify all other images that look the same/similar.
* All images with the same hash gets gathered together, their
  filenames read, and an ID assigned to that hash
* Looking through the list of filenames associated wtih each ID, when there is
  a match in the dataframe, that row will get the ID added.

"""

import shelve
import pandas as pd

data = pd.read_csv('/IMAGE_BOX/rows_with_images.csv')

db = shelve.open('IMAGE_BOX/db.shelve')

klist = list(db.keys())

data['image_hash'] = 0

for key in db.keys():
    for f in db[key]:
        #print(key, f)  # klist is a list containing the hashes
        for index, i in enumerate(data['image_path']):
            if f == i.split('/')[3]: # edited from  if f in i:
                print(f, i.split('/')[3])

              #  print("this contains {} at key {}".format(f, key))
                data.image_hash[index] = key

data.to_csv("IMAGE_BOX/hashedDF.csv", index=False)
