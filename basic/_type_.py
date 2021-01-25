"""
基本数据类型： string，number（整数&浮点数）

"""


def _string_():
    message = "hello world"
    print(message)
    print(message.title())  # 每个单词都首字母大写
    print(message.lower())
    print(message.upper())


def _add_string_():
    first_name = 'hello'
    second_name = 'world'
    print(first_name + ' ' + second_name)
    print('\t' + first_name)  # tab制表符
    print(first_name + '\n' + second_name)  # 换行符
    blank_str = ' hello world '
    print(blank_str.strip())  # 去除开头和末尾空格(不是修改原字符串）
    print(blank_str.lstrip())  # 去除开头空格(不是修改原字符串）
    print(blank_str.rstrip())  # 去除末尾空格(不是修改原字符串）


def _add_number_():
    age = 12
    print('Happy ' + str(age) + 'rd birthday!')


def _add_float_():
    print(0.1 + 0.2)  # 0.30000000000000004


_string_()
_add_string_()
_add_number_()
_add_float_()
