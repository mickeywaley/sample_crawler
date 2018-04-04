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


def start():
    path = '{}/img/'.format(os.path.dirname(__file__))
    print(path)
    pass


def download(url, path):
    img_name = url.split('/')[-1]
    path = '{}/{}'.format(path, img_name)
    r = requests.get(url, stream=True)
    with open(path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=128):
            f.write(chunk)
    print('#save {}'.format(img_name))


if __name__ == '__main__':
    start()
