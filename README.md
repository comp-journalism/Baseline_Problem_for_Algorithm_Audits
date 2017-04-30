#  ARTICLE TITLE

#[The Baseline Problem for Algorithm Audits](https://www.LINK)
By [Jennifer A Stark](https://github.com/JAStark) and [Nick Diakopoulos](http://www.nickdiakopoulos.com)


## The Data
### Collecting data
Data were collected automatically using a web scraper once per day using code based on [this](https://github.com/NikolaiT/GoogleScraper) project. Images were downloaded and related information such as the web link, collection datetime, the search term (e.g. Hillary Clinton, Donald Trump) etc were stored in a MySQL database housed on our AWS space which was then filtered and downloaded as a csv.

### Processed data
Images were all fingerprinted (or hashed) to determine unique images, and count repetitions. A dataframe that includes a hash for each row is [here](https://github.com/comp-journalism/Basline_Problem_for_Algorithm_Audits/blob/master/Data/hashedDF.csv).

#Requirements
If you use the Anaconda distribution, you're all set.

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


#Funding
This project was funded by a grant from the Tow Center for Digital Journalism to study computational and data journalism in the context of algorithmic accountability reporting.

#Feedback
Email Jennifer A Stark at starkja@umd.edu
