# /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
   Description: 
   Author: huangsy
   date: 2018/3/28
"""
__author__ = 'huangsy'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lxml import html


def start():
    driver = webdriver.Chrome()
    driver.get("http://music.163.com/#/discover/playlist")
    print(driver.page_source)
    tree = html.fromstring(driver.page_source)
    res = tree.xpath('//div[@class="g-bd"]//ul[@class="m-cvrlst f-cb"]//img/@src')
    for src in res:
        print(src)


if __name__ == '__main__':
    start()
