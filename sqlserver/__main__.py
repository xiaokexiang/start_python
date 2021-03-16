import json
from datetime import datetime

import pymssql
import requests

article_type = {'工作动态': 0, '通知公告': 1, '图片新闻': 2, '标准征求意见': 3, '国际标准进展': 4}


class Attach:
    def __init__(self, filename, path):
        self.filename = filename
        self.path = path

    def __hash__(self):
        return hash(self.filename + self.path)

    def __eq__(self, other):
        if self.filename == other.filename and self.path == other.path:
            return True
        else:
            return False


def init():
    connection = pymssql.connect(server='10.10.10.7', user='SA', password='Admin123', database='cspiii_stc',
                                 charset='utf8')
    return connection


def query(connection, attach):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM dbo.Article')
    row = cursor.fetchone()
    number = 0
    while row:
        print("No.%d ,ID=%s, Title=%s" % (number, row[0], row[2]))
        number = number + 1
        save(row, attach)
        row = cursor.fetchone()


def query_attachment(connection):
    body = {}
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM dbo.Attachment")  # WHERE FileType != '.jpg'
    row = cursor.fetchone()
    while row:
        value = [] if body.get(row[1]) is None else body.get(row[1])
        value.append(Attach(filename=row[4], path=row[6]))
        body[row[1]] = list(set(value))
        row = cursor.fetchone()
    return body


def save(row, attach):
    global conn
    body = {}
    _type_ = article_type.get(row[31])
    if _type_ is None:
        body['type'] = -1
    else:
        body['type'] = _type_
    if row[2] is None:
        body['title'] = '暂无'
        body['type'] = -1
    else:
        body['title'] = row[2]
    if row[8] == '' or row[8] is None:
        body['author'] = '系统管理员'
    else:
        body['author'] = row[8]
    if row[15] == '' or row[15] is None:
        body['source'] = '其他'
    else:
        body['source'] = row[15]
    body['top'] = False
    if row[9] is None or row[9] == '':
        return
    body['content'] = row[9].encode('latin1').decode('gbk')  # 乱码问题
    if attach.get(row[0]) is not None:
        array = []
        a = {}
        for attach in attach.get(row[0]):
            a['filename'] = attach.filename
            a['path'] = attach.path
            array.append(a)
        body['attachments'] = array
    if row[21] is not None:
        body['banner'] = row[21]
    body['time'] = datetime.timestamp(row[12]) * 1000
    # json_body = json.dumps(body, ensure_ascii=False)
    response = requests.post(url='http://10.10.10.7:8080/v1/private/tc/news/save',
                             json=body, headers={
            'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjY4MjVkNzhjLWJjOTMtNDI1Ny1hNjE3LTY4NTExM2RhZWNhNSJ9.Gu-UVs99zy8hMCWWcBQTUTMP_luJXv4lYPOn6Q5jv_t0Q0tPuneZHh8gERFzrpNrBIkHx4pOE6GgbGHqWQuDfg',
            'Content-Type': 'application/json;charset=UTF-8'})
    if eval(response.content.decode('utf-8'))['code'] != 200:
        print(body.get('title'))


if __name__ == '__main__':
    conn = init()
    attachments = query_attachment(conn)
    query(conn, attachments)
