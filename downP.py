#! /usr/bin/python
#coding=utf-8

import requests
import re
import random

def downloadspic(pic_id_list):
    for pic_id in pic_id_list:       
        for url in (
            'http://www.pixiv.net/member_illust.php?mode=big&illust_id=%s'% pic_id,
        ):
            r = requests.get(url)
            print url

            if r.status_code == 200:
                print 'Find the picture ...'
            else:
                print 'The pictrue is not exsit'


def main():
    i =  range (44686855,44686880)
    downloadspic(i)

if __name__ == "__main__":
    main()
