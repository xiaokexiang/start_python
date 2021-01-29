"""
文件的读取
"""


def _read_file_():
    with open('input.txt') as file_object:
        content = file_object.read()
        print(content)


"""
逐行读取
"""


def _read_file_line_():
    with open('input.txt') as file_object:
        for line in file_object:
            print(line.rstrip())


def _read_to_list():
    with open('input.txt') as file_object:
        lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())


_read_file_()
_read_file_line_()
_read_to_list()
