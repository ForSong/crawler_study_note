# -*- coding: utf-8 -*-
"""
@Time    : 2020/9/12 
@Author  : Zhizhuo Song
@Email   : zhizhuosong@126.com
@File    : szz_12_neihan_spider.py
内涵段子的网站爬取与之前的主要不同点在于，第一页的内容存储在html中，但是后面的内容是
json请求得到的，也就是存储在json中的
"""
import requests
import re
import json


class Neihan:
    def __init__(self):
        self.start_url = '需要请求的内涵段子的地址'
        # 这是下一页的网址
        self.next_url_temp = '需要请求的内涵段子的地址{}'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}

    def parse_url(self, url):
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_first_page_content_list(self, html_str):  # 提取第一页的数据，这里是html字符串
        # 限制条件注意要更严格一些，这样才能更好的定位
        content_list = re.findall(r'<h1 class=\"title\">.*?><p>(.*?)</p>')
        max_time = re.findall("max_time: '(.*?)'", html_str)[0]
        return content_list, max_time

    def get_content_list(self, json_str):  # 提取从第二页开始的json中的数据
        dict_ret = json.loads(json_str)
        data = dict_ret['data']['data']
        content_list = [i['group']['content'] for i in data]
        max_time = dict_ret['data']['max_time']
        has_more = dict_ret['data']['has_more']
        return content_list, max_time, has_more

    def save_content_list(self, content_list):  # 保存
        with open('neihan.txt', 'a', encoding='utf-8') as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write('\n')
        print('保存成功')

    def run(self):  # 实现主要逻辑
        # 1. start_url
        # 2. 发送请求获取响应
        html_str = self.parse_url(self.start_url)
        # 3. 提取数据
        content_list, max_time = self.get_first_page_content_list(html_str)
        # 4. 保存
        self.save_content_list(content_list)
        # 5. 构造下一页的url地址
        # 小技巧，这里没有has_more于是就给他一个假的has_more
        has_more = True
        while has_more:
            next_url = self.next_url_temp.format(max_time)
            # 6. 发送请求，获取响应
            json_str = self.parse_url(next_url)
            # 7. 提取数据，提取max_time
            content_list, max_time, has_more = self.get_content_list(json_str)
            # 8. 保存
            self.save_content_list(content_list)
            # 9. 循环5-8步


if __name__ == '__main__':
    neihan = Neihan()
    neihan.run()
