#! /usr/bin/python
# -*- coding:utf-8 -*-
import os
import sys
from datetime import datetime

from urllib import urlretrieve
import urllib2
from sgmllib import SGMLParser
import pymongo
# import gsidfs

conn = pymongo.Connection('localhost', 27017)
db = conn['spider']
pic = db.pic

reload(sys)
sys.setdefaultencoding('utf-8')


class TitleName(SGMLParser):
    def __init__(self):
        SGMLParser.__init__(self)
        self.is_h1 = ""
        self.name = []

    def start_a(self, attrs):
        global fname, durl
        self.urls = []
        href = [v for k, v in attrs if k=='href' and v.split('.')[-1]=='jpg']

        if href:
            self.urls.extend(href)
            urlretrieve(href[0], '/home/tao/spider/%s'% href[0].split('/')[-1])
            durl = href[0]
            fname = href[0].split('/')[-1]

    def start_h1(self, attrs):
        self.is_h1 = 1

    def end_h1(self):
        self.is_h1 = ""

    def start_img(self, attrs):
        self.imgs = []
        src = [ v for k,v in attrs if k=="src" and v.startswith("http") ]
        if src:
            self.imgs.extend(src)

    def handle_data(self, text):
        if self.is_h1 == 1:
            self.name.append(text)

for sid in range(134000, 135493):
    url_from_sid = 'http://tsundora.com/%d/'% sid

    try:
        content = urllib2.urlopen(url_from_sid, timeout=3).read()
        titlename = TitleName()
        titlename.feed(content)

        for item in titlename.name:
            print item,
            print url_from_sid
            pic.insert({"title" : item, "url" : url_from_sid, "name" : fname, "durl" : durl,"atime" : datetime.now()})

    except Exception as e:
        print e

