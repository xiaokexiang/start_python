"""
http客户端request的使用
"""

import requests


def _get_():
    resp = requests.get('https://github.com/xiaokexiang')
    print(resp.text)


_get_()
