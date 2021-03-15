import os
import shutil


def read(path):
    # 生成归档目录存放归档后文件
    _dir_ = os.path.join(path, '归档')
    if not os.path.exists(_dir_):
        os.mkdir(_dir_)
    other_dir = os.path.join(_dir_, '1.未归档')
    if not os.path.exists(other_dir):
        os.mkdir(other_dir)
    files = os.listdir(path)
    for file in files:  # 遍历文件夹
        if os.path.isfile(os.path.join(path, file)):  # 判断是否是文件夹，不是文件夹才打开
            filename = file.title()
            print("read file " + filename)
            source = os.path.join(path, filename)
            position = get_type(filename)
            if position is None:
                shutil.copyfile(source, other_dir)
                continue
            new_file_name = rename(filename)
            if new_file_name is None:
                shutil.copyfile(source, other_dir)
                continue
            dest_dir = os.path.join(_dir_, position)
            if not os.path.exists(dest_dir):
                os.mkdir(dest_dir)
            dest = os.path.join(dest_dir, new_file_name)
            shutil.copyfile(source, dest)


def rename(filename):
    try:
        suffix = '.' + filename.split(".")[1]
        if '智联' in str(filename):
            name = filename.split("_")
            return name[2] + '_' + name[1] + suffix
        elif '51' in str(filename):
            name = filename.split("_")
            index = name[2].find("(")
            return name[2][:index] + '_' + name[1] + suffix
        else:
            return None
    except Exception as e:
        print('rename error: ', e)
        return None


def get_type(filename):
    try:
        if '智联' in str(filename) or '51job' in str(filename).lower():
            name = filename.split("_")[2].split(".")[0]
            index = name.find("(")
            return name[:index] if index > 0 else name
        else:
            return None
    except Exception as e:
        print('getType error: ', e)
        return None


if __name__ == '__main__':
    _source_dir = input('请输入您需要整理的文件夹路径（例如C:\\简历）： ')
    # _source_dir = "C:\\Users\\xxiao\\Desktop\\3月8号及之前"
    read(_source_dir)
    input('请按回车键推出！')
