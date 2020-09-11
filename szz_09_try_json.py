# -*- coding: utf-8 -*-
"""
@Time    : 2020/9/11 
@Author  : Zhizhuo Song
@Email   : zhizhuosong@126.com
@File    : szz_09_try_json.py
使用loads和dumps实现json字符串和python数据类型之间的转换
json字符串都是双引号
json.load和json.dump与loads和dumps稍有区别，但是区别不大

"""
import json
from parse_url import parse_url
from pprint import pprint

url = '豆瓣手机网站请求，暂时无法打开'
# 调用之前写好的工具可以直接得到字符串
html_str = parse_url(url)

# json.loads将json字符串转换为python类型
ret1 = json.loads(html_str)
# pprint(ret1)
# print(type(ret1))

# json.dumps能够把python类型转化为json字符串
# 一般用于将内容写入json，因为不能直接写入python类型，只能写入字符串
with open('douban.json', 'w', encoding='utf-8') as f:
    # ensure_ascii设置False可以显示出中文，indent=2表示缩进为2
    # 为什么不直接使用str(),是因为我们想使用ensure_ascii和indent这些参数
    f.write(json.dumps(ret1, ensure_ascii=False, indent=2))

with open('douban.json', 'r', encoding='utf-8') as f:
    ret2 = f.read()
    ret3 = json.loads(ret2)
    print(ret3)
    print(type(ret3))

# 使用json.load提取类文件对象的数据
# 与loads的区别是可以直接使用类文件
with open('douban.json', 'r', encoding='utf-8') as f:
    ret4 = json.load(f)
    print(ret4)
    print(type(ret4))

# 使用json.dump写入类文件对象
with open('douban.json', 'w', encoding='utf-8') as f:
    json.dump(ret1, f, ensure_ascii=False, indent=2)
