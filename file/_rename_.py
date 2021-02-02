"""
判断图片的拍摄时间，并拷贝及重命名，生成年-月的文件夹并将文件移动进该文件夹
"""
import os
import shutil
import time


def _rename_to_():
    source = input('Please input source dir: ')
    dest = input('Please input dest dir: ')
    if not os.path.exists(dest):
        os.mkdir(dest)
    count = 0
    for root, dirs, files in os.walk(source, topdown=False):
        for filename in files:
            count = count + 1
            image_time = time.localtime(os.stat(os.path.join(root, filename)).st_mtime)
            dir_time = time.strftime('%Y_%m', image_time)
            suffix = filename.split('.')[1]
            create_time = time.strftime('%Y_%m_%d_%H_%M_%S', image_time)
            new_file_name = create_time + '.' + suffix
            print('No: ' + str(count) + ', origin_name: ' + filename + ', new_name: ' + new_file_name)
            dest_dir = os.path.join(dest, dir_time + '\\')
            if not os.path.isdir(dest_dir):
                os.makedirs(dest_dir)
            shutil.copy(os.path.join(root, filename), os.path.join(dest_dir, new_file_name))


_rename_to_()
