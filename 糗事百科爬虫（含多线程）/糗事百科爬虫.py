# -*- coding: utf-8 -*-
# Created : 2018/8/26 18:33
# author ：GuoLi

import requests
from lxml import etree
import json

class QiushiSpider:
    def __init__(self):
        self.start_url = 'https://www.qiushibaike.com/hot/page/{}/'
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Host": "www.qiushibaike.com",
            "Referer": "https://www.qiushibaike.com/hot/",
        }

    def get_url_list(self):
        return [self.start_url.format(i) for i in range(1, 14)]

    def parse_url(self, url):
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_content_list(self, html_info):
        html = etree.HTML(html_info)
        content_list = []
        div_list = html.xpath("//div[@id='content-left']/div")
        for div in div_list:
            item = {}
            item['name'] = div.xpath(".//div[@class='author clearfix'][1]/a[2]/h2/text()")
            item['name'] = [item['name'][i].replace("\n","") for i in range(len(item['name']))]
            item['info'] = div.xpath(".//div[@class='content']/span/text()")
            item['info'] = [item['info'][i].replace("\n","") for i in range(len(item['info']))]
            item['reader'] = div.xpath(".//div[@class='stats']/span[1]/i/text()")
            item['img'] = div.xpath(".//div[@class='thumb']/a/img/@src")
            item['img'] = "https:" + item['img'][0] if len(item['img']) > 0 else None
            content_list.append(item)
            # print(item)
        return content_list

    def save_content_list(self, content_list):
        for i in content_list:
            with open('qiushi.json','a',encoding="utf-8") as f:
                f.write(json.dumps(i,ensure_ascii=False,indent=4))
                f.write("\n")

    def run(self):
        url_list = self.get_url_list()
        for url in url_list:
            html_info = self.parse_url(url)
            content_list = self.get_content_list(html_info)
            self.save_content_list(content_list)


if __name__ == '__main__':
    qiushi = QiushiSpider()
    qiushi.run()
