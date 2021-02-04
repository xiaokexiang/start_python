"""
csv写入
"""
import csv


class Write:
    def __init__(self, filename):
        self.filename = filename

    def write(self):
        with open(self.filename, 'w', newline='') as f:  # 取消换行
            writer = csv.writer(f)
            for row in [['1', '2', '3'], ['4', '5', '6']]:  # 写入数据到csv
                writer.writerow(row)


if __name__ == '__main__':
    write = Write('output.csv')
    write.write()
