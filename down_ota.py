#! /usr/bin/python
# -*- coding:utf-8 -*-
import urllib2
from sgmllib import SGMLParser


#列出文章标题，方便查找

class TitleName(SGMLParser):
    def __init__(self):
        SGMLParser.__init__(self)
        self.is_h1 = ""
        self.name = []

    def start_h1(self, attrs):
        self.is_h1 = 1

    def end_h1(self):
        self.is_h1 = ""

    def handle_data(self, text):
        if self.is_h1 == 1:
            self.name.append(text)

for uid in range(50630, 50645):
    url_from_uid = 'http://otachan.net/post/show/%d/'% uid
    content = urllib2.urlopen(url_from_uid).read()
    titlename = TitleName()
    titlename.feed(content)

    for item in titlename.name:
        print item,
        print url_from_uid
