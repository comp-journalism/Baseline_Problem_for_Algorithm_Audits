# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 13:02:42 2017

@author: jenniferstark
"""
import requests, time, os
import pandas as pd
from bs4 import BeautifulSoup
import ssl

candidate = 'donald_trump'
html_file = candidate + "_Google_Search_Sept3-Oct28.htm"

candidate_list = []

target_directory = './' + candidate + '_image_universe'
try:
    os.mkdir(target_directory)
except FileExistsError:
    pass

count = 0

with open(html_file) as f:
    soup = BeautifulSoup(f,"html.parser")
    meta_tags = soup.find_all("div", attrs={"class": "rg_meta"})

    for i in meta_tags:
        t = i.get_text()
        split = t.split(',')

        for line in split:

            if line.startswith('"ou":'):
                jpg_url = line
                jpg_url = jpg_url.lstrip('"ou":')

            if line.startswith('"ru":'):
                url = line
                url = url.lstrip('"ru":')

            if line.startswith('"st":'):
                source = line
                source = source.lstrip('"st":')

        if jpg_url and url and source:

            #if "http://" in jpg_url:

            imageFile = str(count) + '_' + candidate + '.jpg'

            current_directory = './'
            path = os.path.join(target_directory)

            with open(os.path.join(path,imageFile), 'wb') as q:
                try:
                    res = requests.get(jpg_url, verify=False)

                    for chunk in res.iter_content(100000):
                        q.write(chunk)
                    print("saving image: " + imageFile + ' count: ' + str(count))
                except ssl.SSLError:
                    pass

            tmp = {}
            tmp['candidate'] = candidate
            tmp['image_file'] = imageFile
            tmp['news_source'] = source
            tmp['news_source_url'] = url
            tmp['image_url'] = jpg_url
            tmp['count'] = count

            old_count = count
            count += 1
            print("Old count: ", old_count, "New count: ", count)

            candidate_list.append(tmp)

        else:
            tmp = {}
            tmp['candidate'] = candidate
            tmp['image_file'] = imageFile
            if source:
                tmp['news_source'] = source
            else: tmp['news_source'] = 'potential_error'

            if url:
                tmp['news_source_url'] = url
            else: tmp['news_source_url'] = 'potential_error'

            if jpg_url:
                tmp['image_url'] = jpg_url
            else:
                tmp['image_url'] = 'potential_error'

            tmp['count'] = count

            old_count = count
            count += 1
            print("Old count: ", old_count, "New count: ", count)

            candidate_list.append(tmp)


        time.sleep(7)

df = pd.DataFrame(candidate_list)
df.to_csv('donald_trump_image_universe.csv', index=False)
