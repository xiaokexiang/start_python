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
    f = open(os.path.join(dest, 'log.txt'), 'a')
    for root, dirs, files in os.walk(source, topdown=False):
        for filename in files:
            count = count + 1
            prefix_dir = 'photo'
            suffix = filename.split('.')[1]
            if suffix.upper() == 'MOV' or suffix.upper() == 'MP4':
                prefix_dir = 'video'
            image_time = time.localtime(os.stat(os.path.join(root, filename)).st_mtime)
            dir_time = time.strftime("%Y-%#m", image_time)  # 存放的文件夹 2020-1 不是 2020-01
            create_time = time.strftime('%Y_%m_%d_%H_%M_%S', image_time)
            new_file_name = 'No_' + str(count) + '_' + create_time + '.' + suffix
            dest_dir = os.path.join(dest, prefix_dir, dir_time + '\\')
            if not os.path.isdir(dest_dir):
                os.makedirs(dest_dir)
            file_name = new_file_name
            if os.path.exists(os.path.join(dest_dir, new_file_name)):
                file_name = 'DUP_' + new_file_name
            print('No: ' + str(count) + ', origin_name: ' + filename + ', new_name: ' + file_name)
            print('No: ' + str(count) + ', origin_name: ' + filename + ', new_name: ' + file_name, file=f)
            shutil.copy(os.path.join(root, filename), os.path.join(dest_dir, file_name))

    f.close()


_rename_to_()
