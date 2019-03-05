# -*- coding: utf-8 -*-
# Created : 2018/8/26 18:33
# author ：GuoLi
from queue import Queue
import requests
from lxml import etree
import json
import threading


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
        self.url_queue = Queue()
        self.html_queue = Queue()
        self.content_queue = Queue()

    def get_url_list(self):
        # return [self.start_url.format(i) for i in range(1, 14)]
        for i in range(1, 14):
            self.url_queue.put(self.start_url.format(i))

    def parse_url(self):
        while True:
            url = self.url_queue.get()
            print(url)
            response = requests.get(url, headers=self.headers)
            # return response.content.decode()
            self.html_queue.put(response.content.decode())
            self.url_queue.task_done()

    def get_content_list(self):
        while True:
            html_info = self.html_queue.get()
            html = etree.HTML(html_info)
            content_list = []
            div_list = html.xpath("//div[@id='content-left']/div")
            for div in div_list:
                item = {}
                item['name'] = div.xpath(".//div[@class='author clearfix'][1]/a[2]/h2/text()")
                item['name'] = [item['name'][i].replace("\n", "") for i in range(len(item['name']))]
                item['info'] = div.xpath(".//div[@class='content']/span/text()")
                item['info'] = [item['info'][i].replace("\n", "") for i in range(len(item['info']))]
                item['reader'] = div.xpath(".//div[@class='stats']/span[1]/i/text()")
                item['img'] = div.xpath(".//div[@class='thumb']/a/img/@src")
                item['img'] = "https:" + item['img'][0] if len(item['img']) > 0 else None
                content_list.append(item)
            self.content_queue.put(content_list)
            self.html_queue.task_done()

    def save_content_list(self):
        while True:
            content_list = self.content_queue.get()
            for i in content_list:
                with open('qiushi_1.json', 'a', encoding="utf-8") as f:
                    f.write(json.dumps(i, ensure_ascii=False, indent=4))
                    f.write("\n")
            self.content_queue.task_done()

    def run(self):
        # url_list = self.get_url_list()
        thread_list = []
        t_url = threading.Thread(target=self.get_url_list)
        thread_list.append(t_url)
        for i in range(3):
            t_parse = threading.Thread(target=self.parse_url)
            thread_list.append(t_parse)

        for i in range(2):
            t_html = threading.Thread(target=self.get_content_list)
            thread_list.append(t_html)

        t_save = threading.Thread(target=self.save_content_list)
        thread_list.append(t_save)
        for t in thread_list:
            t.setDaemon(True)  # 把子线程设置为守护线程，等待队列中的任务完成之后再完成
            t.start()

        for q in [self.url_queue, self.html_queue, self.content_queue]:
            q.join()  # 让主线程阻塞，等待队列中的任务完成之后在完成

        print("结束！")

        # for url in url_list:
        #     html_info = self.parse_url(url)
        #     content_list = self.get_content_list(html_info)
        #     self.save_content_list(content_list)


if __name__ == '__main__':
    qiushi = QiushiSpider()
    qiushi.run()
