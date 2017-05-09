# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 18:22:53 2017

@author: jenniferstark
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 19:20:13 2016

@author: jenniferstark

This script is meant to:

* Each image has a hash which is stored in the shelf
* Using that hash, we can identify all other images that look the same/similar,
cos the hash will be the same/similar
* All images with the same/similar hash gets gathered together, their
  filenames read, and an ID assigned to that hash
* Looking through the list of filenames associated wtih each ID, when there is
  a match in the DF, that row will get the ID added.
* Finally, the ID can get propergated throughout the rest of the DF for rows
  _without_ a downloaded image, based on matching visible links??


ORDER:

0 remove_rejected_from_data.py   (rejected due to image not containing the candidate or image containing mulitple faces)
1 index.py
2 baseline_imagesintoDF.py

"""

import shelve
import pandas as pd

data = pd.read_csv('hillary_clinton_remaining_images.csv')

db = shelve.open('hc_baseline.shelve')

klist = list(db.keys())

data['image_hash'] = 0

for key in db.keys():
    for f in db[key]:
       # print(key, f)# klist is a list containing the hashes
        for index, i in enumerate(data['image_file']):
            if f == i:
                print("DB: ", f, "  image file: ", i)
              #  print("this contains {} at key {}".format(f, key))
                data.image_hash[index] = key
db.close()

data.to_csv("/BASELINE/HC_baseline_hashedDF.csv", index=False)
