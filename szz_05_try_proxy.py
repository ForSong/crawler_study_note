# -*- coding: utf-8 -*-
"""
@Time    : 2020/9/8 
@Author  : Zhizhuo Song
@Email   : zhizhuosong@126.com
@File    : szz_05_try_proxy.py
"""
import requests

proxies = {"http": "http://123.57.76.102:80"}

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}
# 可以使用requests增加
r = requests.get("http://www.baidu.com", proxies=proxies, headers=headers)

print(r.status_code)
