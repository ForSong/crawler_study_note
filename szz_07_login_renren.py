# -*- coding: utf-8 -*-
"""
@Time    : 2020/9/8 
@Author  : Zhizhuo Song
@Email   : zhizhuosong@126.com
@File    : szz_07_login_renre.py
"""
import requests

session = requests.session()
post_url = 'http://www.renren.com/Plogin.do'
post_data = {'email': 'mr_mao_hacker@163.com', 'password': 'alarmchinme'}

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}

# 使用session发送post请求，cookie保存在其中
session.post()
# 再使用session进行请求登录之后才能访问的地址
r = session.get('http://www.renren.com/327550029/profile', headers=headers)

# 保存页面
with open('renren1.html', 'w', encoding='utf-8') as f:
    f.write(r.content.decode())
