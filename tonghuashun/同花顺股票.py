# _*_coding:utf-8 _*_
"""
    @Time　　: 2021/9/11   13:34 
    @Author　 : Guoli
    @ File　　  : 同花顺股票.py
    @Software  : PyCharm
    @Description : 
"""

import requests
from lxml import etree
import time
import execjs


content_list = []


def get_info(url, js):
    # print(js)
    exec = execjs.compile(js)
    cookie = exec.call('get_cookie')
    print(cookie)
    headers = {
        'Accept': 'text/html, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        # 'Cookie': 'v=AwAA; v=A0WQimZ4iPgs0KwkF625ZCLXUop8AvpUQ73d6EeqA5uLZ2v8D1IJZNMG7ajU',
        # 'hexin-v': 'AzXg2taouMhEBtx0QEapFLJnQrrssulbs2bNGLda8az7jlssfwL5lEO23e9E',
        'Cookie': "v=" + cookie,
        'hexin-v': cookie,
        'Host': 'q.10jqka.com.cn',
        'Proxy-Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    global content_list
    res = requests.get(url, headers=headers).text
    # print(res)
    html = etree.HTML(res)
    tr_list = html.xpath("//table/tbody/tr")
    for tr in tr_list:
        name = tr.xpath('./td[3]/a/text()')
        print(name)
        content_list.append(name[0])
    # print(content_list)

for i in range(1, 222):
    with open('./tonghuashun.js', 'r')as f:
        js = f.read()
    url = 'http://q.10jqka.com.cn/index/index/board/all/field/zdf/order/desc/page/{}/ajax/1/'.format(i)
    print(url)
    get_info(url, js)
    time.sleep(1)
print(content_list)



