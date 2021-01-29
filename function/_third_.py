"""
第三方库
"""
from collections import OrderedDict


def print_dict():
    order_dict = OrderedDict({
        'jen': 'python',
        'sarah': 'c++',
        'phil': 'java'
    })
    for k, v in order_dict.items():
        print(k + ': ', v)


print_dict()

