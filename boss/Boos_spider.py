# _*_coding:utf-8 _*_
"""
    @Time　　: 2021/8/9   15:00 
    @Author　 : Guoli
    @ File　　  : 爬虫.py
    @Software  : PyCharm
    @Description : 
"""


import requests
import execjs
import time
import os
import re


class BossSpider():
    def __init__(self):
        self.headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            # 'accept-encoding': 'gzip, deflate, br',
            # 'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            # 'cache-control': 'max-age=0',
            'cookie': '__zp_stoken__=b8acdZ2JbLCRdESB8S0Y4RXwKeXgGC9YN1EBLFtzOCwpY147IgNJVQ1QKE1RIX90Wi5uKGc1SyJLNgoYIF9weFpAED5jPGknWVJuVxB6IVQfSSoSC1lYGzpgOFYMHwQ%2FGBdcAH0%2FNEAJBno%3D',
            # 'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            # 'sec-ch-ua-mobile': '?0',
            # 'sec-fetch-dest': 'document',
            # 'sec-fetch-mode': 'navigate',
            # 'sec-fetch-site': 'same-origin',
            # 'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
        }
        self.session = requests.Session()

    def parse(self, url):
        res = requests.get(url, headers=self.headers)
        print(res.text)
        # print(os.getcwd())

        print(res.url)
        seed_url = res.url.replace('https://www.zhipin.com/web/common/security-check.html', '')
        print(seed_url)
        with open('./Boss/gen_seed', 'r')as f:
            final_js = f.read()
        final_js = final_js.replace("module", 'moduler')
        final_js = final_js.replace("__filename", "__filenamer")
        final_js = final_js.replace("=Buffer", "=Bufferr")
        final_js = final_js.replace("typeof process", "typeof child_process")
        final_js = re.sub("this===(.*?),", "true,", final_js)
        js_p = execjs.compile(final_js)
        code = js_p.call('get_cookie', seed_url)
        self.headers['cookie'] = code
        print(self.headers)
        
        time.sleep(3)
        self.parse(url)




    def main(self):
        url = 'https://www.zhipin.com/job_detail/?query=python&city=101190400&industry=&position='
        self.parse(url)


if __name__ == '__main__':
    boss = BossSpider()
    boss.main()
