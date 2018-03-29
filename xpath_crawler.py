# /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
   Description: 
   Author: huangsy
   date: 2018/3/28
"""
__author__ = 'huangsy'

import requests
from lxml import html


def start():
    head = {
        'User-Agent': 'Mozilla/5.0(Macintosh;Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
    }
    resp = requests.get('http://jandan.net/ooxx', headers=head)
    if resp.status_code == 200:
        print(resp.content)
        tree = html.fromstring(resp.content)
        target = tree.xpath('//div[@class="content"]//a[@hidefocus="true"]/img/@src')
        for t in target:
            print("feiyu.com/{}".format(t))
    else:
        print(resp.status_code)


if __name__ == '__main__':
    start()