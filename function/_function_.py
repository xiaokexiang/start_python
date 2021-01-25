def say(username):
    print('say: ' + username)


def _say_(username='nothing'):  # 默认值
    print('say: ' + username)


def _format_(name=''):
    return name.lower().title()  # 函数可返回任意类型的数据


def _any_arg_(*args):  # 任意数量的参数会被封装到tuple中,且放到最后
    print(args)
    for a in args:
        print(a)


def _key_arg_(**kwargs):  # 关键字参数会将传入的参数封装到dict中
    for k, v in kwargs.items():
        print('key: ' + k + ' ,value: ' + v)


say('hello')
say(username='hello')
_say_()
print(_format_("LUCY SAN"))
_any_arg_(1, 2, 3, 4, 5)
_key_arg_(name='lucky', second_name='lee')
