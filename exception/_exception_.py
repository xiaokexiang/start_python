"""
异常
"""


def _file_not_found_exception_():
    try:
        with open('hello.txt') as file_object:
            content = file_object.read()
    except FileNotFoundError:
        print('file not found')
    else:
        print(content)


_file_not_found_exception_()
