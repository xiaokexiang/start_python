def _list_():
    print('--------------- 列表 ---------------')
    collection = ['hello', 'world', 'ya']
    print(collection)
    print(collection[0])
    print(collection[-1])
    collection.append('!')  # 追加到队尾
    print(collection)
    collection.insert(0, 'say')  # 指定位置插入
    print(collection)
    del collection[0]  # 删除第一个元素
    c = collection.pop()  # 弹出（删除）指定位置的元素（默认队尾）
    print(c)
    collection.remove('hello')  # 根据值删除元素，只会删除第一个符合的元素
    print(collection)


def _sort_list_():
    print('--------------- 列表排序 ---------------')
    collection = ['say', 'hello', 'world', 'ya']
    print(sorted(collection))  # 临时排序
    print(collection)
    collection.sort()  # 永久排序
    print(collection)
    collection.reverse()
    print(collection)  # 倒序


def _len_list():
    print('--------------- 列表长度 ---------------')
    collection = ['say', 'hello', 'world', 'ya']
    print(len(collection))
    print(collection.__len__())


def _iter_():
    print('--------------- 列表遍历 ---------------')
    collection = ['say', 'hello', 'world', 'ya']
    for c in collection:
        print(c)


def _range_():
    print('--------------- range ---------------')
    for i in range(1, 5):  # 左闭右开
        print(i)
    for x in range(1, 10, 3):  # [1,10)开始＋3直到10
        print(x)
    print(list(range(10, 15, 2)))  # [10, 12, 14]


def _calc_():
    print('--------------- 列表简单统计 ---------------')
    digits = list(range(1, 11))
    print(max(digits))
    print(min(digits))
    print(sum(digits))


def _comprehension_():
    print('--------------- 列表解析 ---------------')
    squares = [value ** 2 for value in range(1, 10)]  # [1, 4, 9, 16, 25, 36, 49, 64, 81]
    print(squares)


def _slice_():
    print('--------------- 列表切片 ---------------')
    squares = [value ** 2 for value in range(1, 10)]
    print(squares[0:3])  # 左闭右开 0,1,2
    print(squares[:4])  # 左闭右开 0,1,2,3
    print(squares[6:])  # 左闭右开 6,-1
    print(squares[-1:])  # 输出最后一个
    print(squares[-3:])  # 输出最后三个


def _copy_():
    source = [1, 2, 3]
    dest = source[:]
    source.append(4)
    dest.append(-1)
    print(source)
    print(dest)


_list_()
_sort_list_()
_len_list()
_iter_()
_range_()
_calc_()
_comprehension_()
_slice_()
_copy_()