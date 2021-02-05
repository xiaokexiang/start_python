"""
http客户端request的使用
"""

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132'
}
proxies = {
    'http': '176.235.99.13:9090'
}


def _get_():
    resp = requests.get('https://github.com/xiaokexiang', headers=headers, proxies=proxies)
    # 指定响应编码
    print('请求响应的编码： ', resp.encoding)
    with open('github.html', 'w', encoding=resp.encoding) as f:
        f.write(resp.text)


def _session_():
    session = requests.session()  # 某些共性接口使用同一个session，避免多次指定参数或header
    session.headers = headers
    session.proxies = proxies
    resp = session.get('https://github.com/xiaokexiang')
    print(resp.text)


_session_()
