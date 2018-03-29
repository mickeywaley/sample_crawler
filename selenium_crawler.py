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
    # driver.implicitly_wait(10)
    driver.get("http://music.163.com/#/discover/playlist")
    # try:
        # element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'g-bd')))
    #     driver.implicitly_wait(10)
    # except Exception as e:
    #     print(e)
    # finally:
    #     driver.quit()
    print(driver.page_source)
    # tree = html.fromstring(driver.page_source)
    # res = tree.xpath('/iframe[@id="g_iframe"]')
    # print(res)
    # for src in res:
    #     print(src)


if __name__ == '__main__':
    start()
