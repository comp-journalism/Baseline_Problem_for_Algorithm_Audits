#  "Using Baselines for Algorithm Audits" submitted to [European Data and Computational Journalism Conference, 2017](http://datajconf.com)

## By [Jennifer A Stark](https://github.com/JAStark) and [Nick Diakopoulos](http://www.nickdiakopoulos.com)


## The Data
### Collecting data
Data were collected automatically using a web scraper once per day using code based on [this](https://github.com/NikolaiT/GoogleScraper) project. Images were downloaded and related information such as the web link, collection datetime, the search term (e.g. Hillary Clinton, Donald Trump) etc were stored in a MySQL database housed on our AWS space which was then filtered and downloaded as a csv.

### Processed data
Baseline image processing can be found in `BASELINE` directory, while data processing for `image box` images, found on the main Google search results page, are in `IMAGE_BOX`.

Analysis is divided up into analysing the images themselves for sentiment using the Microsoft APIs, and analysing the sources of the images (e.g. Business Insider, Breitbart, Salon). News source main analysis can be found in `Statistics.ipynb` in the main directory.

## Requirements

* Python 3
* ipython notebook / Jupyter
* pandas
* numpy
* matplotlib.pyplot
* json
* shelve
* PIL
* imagehash
* argparse
* GoogleScraper


## Funding
This project was funded by a grant from the Tow Center for Digital Journalism to study computational and data journalism in the context of algorithmic accountability reporting.

## Feedback
Email Jennifer A Stark at starkja@umd.edu
