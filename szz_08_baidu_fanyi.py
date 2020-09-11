# -*- coding: utf-8 -*-
"""
@Time    : 2020/9/11 
@Author  : Zhizhuo Song
@Email   : zhizhuosong@126.com
@File    : szz_08_baidu_fanyi.py
"""
import requests
import json
# import sys


class BaiduFanyi:
    def __init__(self, trans_str):
        self.lang_detect_url = 'https://fanyi.baidu.com/langdetect'
        self.trans_url = 'https://fanyi.baidu.com/basetrans'
        self.trans_str = trans_str
        self.headers = {
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}

    # 因为步骤1.2和步骤3中都有发送post请求获取响应的方法，因此单独定义一个方法
    def parse_url(self, url, data):  # 发送post请求
        response = requests.post(url, data=data, headers=self.headers)
        # 因为两次请求都需要把字符串转换为字典，因此可以直接在这个方法中写
        return json.loads(response.content.decode())

    def get_ret(self, dict_response):  # 提取翻译的结果
        ret = dict_response['trans'][0]['dst']
        print(ret)

    def run(self):  # 实现主要逻辑
        # 主逻辑中的语句是否抽取取决于是否能在一两句只能写完，如果能就不用抽取，例如第41行
        # 如果不能就需要抽取
        # 1. 获取需要翻译的语言类型
        # 1.1 准备POST的url地址，post_dat
        lang_detect_data = {'query': self.trans_str}
        # 1.2 发送post请求，获取响应
        lang_type = self.parse_url(self.lang_detect_url, lang_detect_data)['lan']
        # 1.3 提取语言类型
        # 2. 准备Post数据
        trans_data = {'query': self.trans_str, 'from': 'zh', 'to': 'en'} if lang_type == 'zh' \
            else {'query': '你好', 'from': 'en', 'to': 'zh'}
        # 3. 发送Post请求获取响应
        dict_response = self.parse_url(self.trans_url, trans_data)
        print(dict_response)
        # 4. 提取数据（翻译的结果）
        self.get_ret(dict_response)


if __name__ == '__main__':
    # trans_str = sys.argv[1]
    trans_str = input('请输入想要翻译的内容（中/英）：')
    fanyi = BaiduFanyi(trans_str)
    fanyi.run()
