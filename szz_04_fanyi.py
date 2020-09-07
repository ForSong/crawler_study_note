# -*- coding: utf-8 -*-
"""
@Time    : 2020/9/7 
@Author  : Zhizhuo Song
@Email   : zhizhuosong@126.com
@File    : szz_04_fanyi.py
"""

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}

data = {
    "from": "en",
    "to": "zh",
    "query": "ho",
    "transtype": "translang",
    "simple_means_flag": "3",
    "sign": "709261.930236",
    "token": "355d014b434bb50d536467379e9f5afc",
    "domain": "common",
}

post_url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

response = requests.post(post_url, data=data, headers=headers)

print(response.content.decode())
