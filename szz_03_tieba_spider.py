# -*- coding: utf-8 -*-
"""
@Time    : 2020/9/7 
@Author  : Zhizhuo Song
@Email   : zhizhuosong@126.com
@File    : szz_03_tieba_spider.py
首先定义一个类，然后写一个run方法，在init方法中先写pass，后续如果有需要添加到init中的内容在进行添加
run方法中主要是写逻辑思路，然后将每一步抽取出来，写成方法。实现完每个步骤就完成了整个
"""
import requests




class TiebaSpider:
    def __init__(self, tieba_name):
        # 如果后面用不到这个变量这一行是可以不用写的
        self.tieba_name = tieba_name
        self.url_temp = 'https://tieba.baidu.com/f?kw=' + tieba_name + '&ie=utf-8&pn={}'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}

    def get_url_list(self):  # 1. 构造url列表
        # url_list = []
        # # 爬取10页
        # for i in range(10):
        #     # 这里的50是通过观察贴吧的url得出的结论
        #     url_list.append(self.url_temp.format(i * 50))
        # return url_list
        # 下面这一行使用的是
        # 字典推导式，列表推导式
        # 扁平胜于嵌套
        return [self.url_temp.format(i * 50) for i in range(100)]

    def parse_url(self, url):  # 2. 发送请求，获取响应
        print(url)
        response = requests.get(url, headers=self.headers)
        # 返回响应的字符串
        return response.content.decode()

    def save_html(self, html_str, page_number):  # 保存html字符串
        file_path = "{}-第{}页.html".format(self.tieba_name, page_number)
        # 一般字符串写入的时候会加上utf-8防止编码错误
        with open(file_path, 'w', encoding="utf-8") as f:  # 李毅-第一页.html
            f.write(html_str)

    def run(self):  # 实现主要逻辑
        # run方法中只写每一步的实现逻辑，不写具体实现的方法，需要实现的
        # 内容再把代码
        # 1. 构造url列表
        url_list = self.get_url_list()
        # 2. 遍历，发送请求，获取响应
        for url in url_list:
            html_str = self.parse_url(url)
            # 3. 保存
            # url_list.index(url)索引位置
            page_number = url_list.index(url) + 1
            self.save_html(html_str, page_number)


if __name__ == '__main__':
    tieba_spider = TiebaSpider("李毅")
    tieba_spider.run()
