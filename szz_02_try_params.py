# -*- coding: utf-8 -*-
"""
@Time    : 2020/9/7 
@Author  : Zhizhuo Song
@Email   : zhizhuosong@126.com
@File    : szz_02_try_params.py
"""
import requests

headers = {
    "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}

# p = {"wd": "测试参数"}
# url_temp = "http://www.baidu.com"
#
# response = requests.get(url_temp, headers=headers, params=p)
# print(response.status_code)
# # 带有很多百分号，就是进了url编码，可以在线解析看到结果
# print(response.request.url)

url = "https://www.baidu.com/s?wd={}".format('测试')
response = requests.get(url, headers=headers)
print(response.status_code)
print(response.request.url)
