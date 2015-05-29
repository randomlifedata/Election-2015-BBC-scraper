# Election-2015-BBC-scraper
A scraper for gathering detailed election results data from the BBC website, using Scrapy.

Contents
========

The Scrapy code is within the directory named election2015. 

Files of note:

1. election2015/scrapy.cfg - the configuration file that tells scrapy this is a project
2. election2105/constituencies.csv - this csv file contains a list of constituency codes that are used to populate the URL list for scraping
3. conversion/election-json-csv.py - this file converts the JSON output to CSV


The output (if you don't want to run the code yourself) is in the folder named 'data'


Scrapy spiders
==============
There are 2 spiders coded here. 

1. bbcparty - returns all parties for all constituencies

one returned item contains constituency code, constituency turnout, party name, party candidate, party number of votes,  party share of vote and party swing

2. bbcconst - returns data for main Westminster parties (CON, LAB, SNP, LIB DEM (LD), GREEN, UKIP ), grouped for each constituency

one returned item contains constituency code, constituency turnout, majority party, and for the main parties: number of votes, vote-share, vote swing and candidate 

Installation
============

To run the code, you must have Scrapy installed. Please see the instructions at http://doc.scrapy.org/en/latest/intro/install.html
If you have pip then you can install it with 

```
pip install scrapy
```

Clone all files from this repo to your own system, then simply navigating to the folder containing scrapy.cfg ought to allow you to peform scrapy actions on this project. 


Running the code
================

With Scrapy installed, navigate to the directory containing scrapy.cfg (and constituencies.csv and a folder also called election 2015).

To use the spider that pulls out all party information - bbcparty - the following command will output the data as JSON and put it in the data folder:
```
scrapy crawl bbcparty -o ../data/party.json
````

To use the spider that pulls out the major  party information, grouped by constituency - bbcconst - the following command will output the data as JSON and put it in the data folder:
```
scrapy crawl bbcconst -o ../data/const.json
```

Convert to CSV
==============
It would be possible to have scrapy output CSV but it's just as easy to use a conversion tool, leaving the scrapy instructions universal. To convert the output JSON files to CSV, use the conversion tool at conversion/election-json-csv.py with the following command structure (if all files are in same directory):
```
python election-json-csv.py --json party.json --csv party.csv
```
