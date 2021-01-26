from _dog_ import Dog

"""
实例属性
"""


class Constant:
    def __init__(self, constant=''):
        self.constant = constant

    def desc(self):
        print(self.constant)


"""
继承父类的子类
"""


class DogSon(Dog):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.constant = Constant('hello world')

    def sit(self):
        print('son ...')
        super().sit()


def _class_():
    dog = Dog('gee', 10)
    dog.roll_over()
    dog.sit()

    son = DogSon('son', 1)
    son.sit()
    son.roll_over()
    son.constant.desc()


_class_()
