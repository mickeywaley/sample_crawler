# /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
   Description: 
   Author: huangsy
   date: 2018/4/4
"""
__author__ = 'huangsy'

import requests
import os
from selenium import webdriver
from lxml import html
import re
import time
from fake_useragent import UserAgent
import asyncio
import threading
import random
import urllib3


def start():
    path = os.path.join(os.path.abspath(os.curdir), 'img')
    if not os.path.exists(path):
        os.mkdir(path)
    url = 'http://www.mmjpg.com/'
    img_urls = catch1(url)
    for img_url in img_urls:
        download(img_url, path)
        second = random.randint(1, 5)
        time.sleep(second)


def catch(url):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(url)
    tree = html.fromstring(driver.page_source)
    imgs = tree.xpath('//div[@pic]//img/@src')
    return [img for img in imgs if re.match(r'^(http|https)[a-zA-Z0-9\.\-\:\/]+\.jpg$', img)]


def catch1(url):
    resp = requests.get(url)
    tree = html.fromstring(resp.content)
    imgs = tree.xpath('//div[@class="pic"]//img/@src')
    return [img for img in imgs if re.match(r'^(http|https)[a-zA-Z0-9\.\-\:\/]+\.jpg$', img)]


def download(url, path):
    try:
        print('#start download {}'.format(url))
        img_name = url.split('/')[-1]
        path = '{}/{}'.format(path, img_name)
        if os.path.exists(path):
            print('#exist')
            return
        fa = UserAgent()
        headers = {'User-Agent': fa.random,
                   'Referer': 'http://img.mmjpg.com'}
        http = urllib3.PoolManager()
        resp = http.request('GET', url, headers=headers, timeout=10, retries=3)
        with open(path, 'wb') as f:
            f.write(resp.data)
        print('#save')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    start()
