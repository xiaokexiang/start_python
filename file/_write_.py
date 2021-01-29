"""
文件写入
'w' 写入模式
'r' 读取模式
'a' 追加模式
'r+' 读取+写入
"""


def _write_file_():
    with open('output.txt', 'w') as file_object:  # 如果文件已存在那么会覆盖原有的文件
        file_object.write('hello world\r')
        file_object.write('ya!')


def _write_file_append_():
    with open('output.txt', 'a') as file_object:
        file_object.write('!')


_write_file_()
_write_file_append_()
