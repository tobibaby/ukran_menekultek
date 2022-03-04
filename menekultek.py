#!/usr/bin/python3

import urllib.request
import datetime
from pprint import pprint
from html_table_parser.parser import HTMLTableParser
import pandas as pd


def url_get_contents(url):

    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)
    return f.read()

xhtml = url_get_contents('https://data2.unhcr.org/en/situations/ukraine').decode('utf-8')

p = HTMLTableParser()

p.feed(xhtml)

date=datetime.datetime.now()
date=str(date)
data=pd.DataFrame(p.tables[0])
data.to_csv ('/home/user/mappa/' + date + 'file_neve.csv', index = False)
