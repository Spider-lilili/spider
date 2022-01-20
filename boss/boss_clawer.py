import re
from urllib.parse import unquote
from requests.api import patch
from requests.sessions import session
from urllib3 import disable_warnings, response
import execjs
from requests import Session


disable_warnings()
session = Session()
with open('./headers.js', 'r')as f:
    raw_js = f.read() + '\n'
tail_js = """
function get_token(seed, ts){
    var code = (new window.ABC).z(seed, parseInt(ts));
    console.log(code);
    return encodeURIComponent(code);
}
"""
url = 'https://www.zhipin.com/job_detail/?query=%E7%88%AC%E8%99%AB&city=101190400&industry=&position='

payload = {}
headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            # 'cookie': '__zp_stoken__=b8acdZ2JbLCRdESB8S0Y4RXwKeXgGC9YN1EBLFtzOCwpY147IgNJVQ1QKE1RIX90Wi5uKGc1SyJLNgoYIF9weFpAED5jPGknWVJuVxB6IVQfSSoSC1lYGzpgOFYMHwQ%2FGBdcAH0%2FNEAJBno%3D',
            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
        }
count = 0
success = 0
while 1:
    session.headers = headers
    response = session.request("GET", url, data=payload, verify=False)
    # local = response.history[0].headers.get("location")
    local = response.url
    print(local)
    seed = unquote(re.findall('seed=(.*?)&', local)[0])
    ts = re.findall('ts=(.*?)&', local)[0]
    filename = re.findall("name=(.*?)&", local)[0]
    ak_url = "https://www.zhipin.com/web/common/security-js/{}.js".format(filename)
    response_ak = session.request("GET", ak_url, data=payload, verify=False)
    final_js = raw_js + response_ak.content.decode() + tail_js
    final_js = final_js.replace("module", 'moduler')
    final_js = final_js.replace("__filename", "__filenamer")
    final_js = final_js.replace("=Buffer", "=Bufferr")
    final_js = final_js.replace("typeof process", "typeof child_process")
    final_js = re.sub("this===(.*?),", "true,", final_js)
    ff = execjs.compile(final_js)
    zp_token = ff.call('get_token', seed, ts)
    cookie = {'__zp_stoken__': zp_token}
    print("zp_token:", zp_token)
    print(cookie)
    response = session.request("GET", url, data=payload, verify=False, cookies=cookie)
    print(response.content.decode())
    if "BOSS直聘" in response.content.decode():
        success += 1
    count += 1
    print("总次数：{}, 成功次数：{}".format(count, success))