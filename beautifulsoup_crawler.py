# /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
   Description: 
   Author: huangsy
   date: 2018/3/31
"""
__author__ = 'huangsy'

from bs4 import BeautifulSoup
from selenium import webdriver


def start():
    url = 'http://huaban.com/'
    driver = webdriver.Chrome()
    driver.get(url)
    html = driver.page_source
    # print(html)
    bs = BeautifulSoup(html)
    # print(bs.title)
    print(bs.find_all('img'))


if __name__ == '__main__':
    start()
