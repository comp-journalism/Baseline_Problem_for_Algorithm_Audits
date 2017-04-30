# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 20:26:16 2017

@author: jenniferstark
"""

import os
import pandas as pd


def make_file_list(candidate):
    flist = []

    file_dir = './' + candidate + "_image_universe"
    csv_file = candidate + '_image_universe.csv'
    output_file = candidate + '_remaining_images.csv'

    for filename in os.listdir(file_dir):
        flist.append(filename)


    data = pd.read_csv(csv_file)

    data['present'] = 0

    for index, i in enumerate(data['image_file']):
        if i in flist:
            data.present[index] = 1
        else: data.present[index] = 0

    data = data[data.present == 1]
    data.to_csv(output_file)

    return data


make_file_list('donald_trump')
