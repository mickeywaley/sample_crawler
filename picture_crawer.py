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


def start():
    path = os.path.join(os.path.abspath(os.curdir), 'img')
    if not os.path.exists(path):
        os.mkdir(path)
    url = 'http://www.mmjpg.com/'
    img_urls = catch1(url)
    count = 0
    for img_url in img_urls:
        download(img_url, path)
        count += 1
        if (count % 3) == 0:
            time.sleep(3)
    # print(img_urls)
    # for i in range(0, 3):
    #     download(img_urls[i], path)


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
    print('#start download {}'.format(url))
    img_name = url.split('/')[-1]
    path = '{}/{}'.format(path, img_name)
    if os.path.exists(path):
        return
    fa = UserAgent()
    headers = {'User-Agent': fa.random,
               'Referer': 'http://img.mmjpg.com'}
    r = requests.get(url, stream=True, headers=headers)
    with open(path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=32):
            f.write(chunk)
    print('#save {}'.format(url))


if __name__ == '__main__':
    start()
