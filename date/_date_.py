"""
日期格式化
%A 星期名称：monday
%B 月份名称：July
%Y 年份：2015
%y 年份： 15
%m 月份： 01-12
%d 天： 01-31
%H 24小时：00-23
%M 分钟：00-59
%S 秒钟00-61
%I 12小时：01-12
%p am/pm
"""
import time
from datetime import date, datetime


class DateTimeTest:

    def __init__(self, date, _type_):
        self.date = date
        self.type = _type_

    def format(self):
        print(datetime.strptime(self.date, self.type))


if __name__ == '__main__':
    today = datetime.today()
    print(today)  # 2021-02-04 11:48:46.546177
    print(today.year)  # 2021
    print(today.__getattribute__('year'))  # 2021
    print(date(2021, 5, 1).__le__(date(2021, 10, 12)))  # 比较日期大小 True
    print(date(2021, 5, 1).__sub__(date(2021, 10, 12)).days)  # 比较日期差距 -164
    print(today.strftime('%Y-%m-%d'))  # date -> str 2021-02-04
    print(today.strftime('%Y-%#m-%d'))  # 2021-2-04 会去除0
    print(today.strftime('%A'))  # Thursday 星期几
    print(today.__format__('%Y-%m-%d'))  # 与strftime()等价
    print(today.__str__())  # 直接转换成字符串
    print(time.time())  # 输出时间戳 秒级 + 毫秒
    print(date.fromtimestamp(time.time()))  # 从时间戳读取成date
    print(today.ctime())  # Thu Feb  4 15:51:42 2021
    print(datetime.strptime('2021-2-04', '%Y-%m-%d'))  # str -> date 2021-02-04 00:00:00
