class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + 'is now sitting!')

    def roll_over(self):
        print(self.name.title() + ' rolled over!')


def _class_():
    dog = Dog('gee', 10)
    dog.roll_over()
    dog.sit()


_class_()
