# -*- coding: utf-8 -*-
"""
@Time    : 2020/9/11
@Author  : Zhizhuo Song
@Email   : zhizhuosong@126.com
@File    : szz_11_douban_spider.py
"""
import requests
import json


class DoubanSpider:
    def __init__(self):
        self.start_url_temp_list = [
            'https://m.douban.com/rexxar/api/v2/subject_collection/tv_american/items?os=ios&for_mobile=1&callback=jsonp1&start=0&count={}&loc_id=108288&_=0',
            '',
            ''
            ]
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}

    def parse_url(self, url):
        print('url')
        response = requests.get(url, headers=self.headers, verify=False)
        return response.content.decode()

    def get_content_list(self, json_str):
        print(json_str)
        dict_ret = json.loads(json_str)
        print(dict_ret)
        content_list = dict_ret['subject_collection_items']
        total = dict_ret['total']
        return content_list, total

    def save_content_list(self, content_list):
        # 注意这里打开文件在上面，这样的作用是可以减少IO次数，从而加快速度
        with open('douban.txt', 'a', encoding='utf-8') as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                # 写入换行符，进行换行
                f.write('\n')
        print('保存成功')

    def run(self):  # 实现主要逻辑
        for url_temp in self.start_url_temp_list:
            num = 0  # 当前页码数
            total = 100  # 假设有第一页，这里需要一个假数字
            # 1. start url
            while num < total + 18:
                url = url_temp.format(num)
                # 2. 发送请求，获取响应
                json_str = self.parse_url(url)
                # 3. 提取数据
                content_list, total = self.get_content_list(json_str)
                # 4. 保存
                self.save_content_list(content_list)
                # if len(content_list) < 18:
                #     break
                # 5. 构造下一页的url地址，进入循环
                num += 18


if __name__ == '__main__':
    douban_spider = DoubanSpider()
    douban_spider.run()
