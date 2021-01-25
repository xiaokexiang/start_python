def _dict_():
    print('--------------- dict ---------------')
    d = {'key': 'hello', 'value': 'world'}
    print(d['key'])
    print(d['value'])


def _add_dict_():
    print('--------------- add dict ---------------')
    d = {'key': 'hello', 'value': 'world'}
    print(d['key'])
    d['score'] = '!'
    print(d)


def _del_dict_():
    print('--------------- del dict ---------------')
    d = {'key': 'hello', 'value': 'world', 'score': '!'}
    del d['score']
    print(d)


def _iter_dict_():
    print('--------------- iter dict ---------------')
    d = {'key': 'hello', 'value': 'world', 'score': '!'}
    for k, v in d.items():  # 可以输出key，value
        print(k, v)
    for k in d:  # 默认输出key
        print(k)
    for k in d.keys():
        print(k)
    for v in d.values():
        print(v)


def _set_():
    print('--------------- set dict ---------------')
    d = {'key': 'hello', 'value': 'world', 'key': '!'}
    for k in set(d.keys()):
        print(k)


_dict_()
_add_dict_()
_del_dict_()
_iter_dict_()
_set_()