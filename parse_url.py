# -*- coding: utf-8 -*-
"""
@Time    : 2020/9/11 
@Author  : Zhizhuo Song
@Email   : zhizhuosong@126.com
@File    : parse_url.py
因为需要频繁的进行请求和获取请求结果，因此将对应的方法抽取出来，单独写一个方法
"""

import requests
from retrying import retry

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}


# retry方法可以多次执行
@retry(stop_max_attempt_number=3)
def _parse_url(url, method, data, proxies):
    if method == 'POST':
        requests.post(url, data=data, headers=headers, proxies=proxies)
    else:
        requests.get(url, headers=headers, proxies=proxies)

    response = requests.get(url, headers=headers, timeout=3)
    assert response.status_code == 200
    return response.content.decode()


def parse_url(url, method='GET', data=None, proxies=None):
    if proxies is None:
        proxies = {}
    try:
        html_str = _parse_url(url, method, data, proxies)
    except Exception:
        html_str = None
    return html_str


if __name__ == '__main__':
    url = 'http://www.baidu.com'
    print(parse_url(url))
