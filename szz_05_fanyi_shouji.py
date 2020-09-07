# -*- coding: utf-8 -*-
"""
@Time    : 2020/9/7 
@Author  : Zhizhuo Song
@Email   : zhizhuosong@126.com
@File    : szz_05_fanyi_shouji.py
利用百度的接口来判断需要翻译内容的语言。即使是英文也可以
"""

import requests
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}

data = {"query": "哈哈12j"}
post_url = "https://fanyi.baidu.com/langdetect"

response = requests.post(post_url, headers=headers, data=data)

# 返回的内容是json字符串，转换为字典
r = response.content.decode()
dict_re = json.loads(r)
# 字典中根据键提取值
language = dict_re['lan']
# print(type(language))
if 'zh' == language:
    print("中文")
