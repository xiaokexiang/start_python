"""
json的操作
"""
import decimal
import json


def loads_str():
    data = '{"name": "lc","price": 18.123}'
    dict_data = dict(json.loads(data, parse_float=decimal.Decimal))  # loads 加载字符串
    for key, value in dict_data.items():
        print(key, value)


def load_stream():
    with open('data.json', 'r') as f:
        content = json.load(f)  # load加载文件流
        for key, value in dict(content).items():
            print(key, value)


def dumps_str():
    dict_data = {"name": "lc", "age": 18}
    data = json.dumps(dict_data)  # dict -> str
    print(data)


def dump_file():
    dict_data = {"name": "lc", "age": 18}
    json.dump(dict_data, open('dump_data.json', 'w'))  # dict -> file


loads_str()
