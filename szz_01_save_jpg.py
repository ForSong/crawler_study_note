# -*- coding: utf-8 -*-
"""
@Time    : 2020/9/7
@Author  : Zhizhuo Song
@Email   : zhizhuosong@126.com
@File    : szz_01_save_jpg.py
"""

import requests

# 发送请求
r = requests.get('https://requests.readthedocs.io/zh_CN/latest/_static/requests-sidebar.png')

# 保存, wb 表示要写入的内容是二进制的文件
# 为什么不能用w，因为w就会写入字符串的形式，内存中应该是二进制的内容，写入
# 应该是二进制的内容，保存二进制的内容到本地，使用wb
# 注意后缀需要修改
with open('a.png', 'wb') as f:
    f.write(r.content)
