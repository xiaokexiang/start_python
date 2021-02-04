"""
读取csv
"""

import csv


class Read:
    def __init__(self, filename):
        self.filename = filename

    def file_header(self):
        with open(self.filename, encoding='utf-8') as f:
            reader = csv.reader(f)
            header_row = next(reader)
            for index, column in enumerate(header_row):
                print(index, column)  # 输出csv的header

    def file_data(self):
        with open(self.filename, encoding='utf-8') as f:
            reader = csv.reader(f, 1)
            next(reader)  # 为了跨过第一行
            row_one = []
            for row in reader:
                row_one.append(row[1])
            print(row_one)


if __name__ == '__main__':
    read = Read('input.csv')
    read.file_data()
