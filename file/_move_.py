import os
import shutil

"""
将当前目录下的文件或文件夹内的文件（包含子文件夹）保存到指定目录
"""


def _move_():
    source = input('Please input source dir: ')
    dest = input('Please input dest dir: ')
    log_name = os.path.join(dest, 'move.log')
    if not os.path.exists(dest):
        os.mkdir(dest)
    f = open(log_name, mode='a')
    count = 0
    for root, dirs, files in os.walk(source, topdown=False):
        for filename in files:
            if filename != '_move_.py':
                count = count + 1
                cp_source = os.path.join(root, filename)
                if os.path.exists(os.path.join(dest, filename)):  # 判断文件名是否重复
                    cp_dest = os.path.join(dest, 'DUP_' + filename)
                    print('No: ' + str(count) + '; source: ' + cp_source + ', dest: ' + cp_dest, file=f)
                    shutil.move(cp_source, cp_dest)
                else:
                    cp_dest = os.path.join(dest, filename)
                    print('No: ' + str(count) + '; source: ' + cp_source + ', dest: ' + cp_dest, file=f)
                    shutil.move(cp_source, cp_dest)
    f.close()


_move_()
