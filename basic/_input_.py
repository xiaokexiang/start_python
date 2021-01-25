"""
获取用户的输入
"""


def _input_():
    message = input("what's your name: ")
    print('hello: ' + message)


def _input_while_():
    message = ""
    while message != 'quit':
        message = input("please input something: ")
        if message != 'quit':
            print(message)


def _input_while_true_():
    while True:
        message = input("what's your name? ")
        if message == 'quit':
            break
        print(message)


_input_()
_input_while_()
_input_while_true_()
