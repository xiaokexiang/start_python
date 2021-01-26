"""
父类：必须位于子类之前且和子类在同一文件中(或通过import)
"""


class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + ' is now sitting!!')

    def roll_over(self):
        print(self.name.title() + ' rolled over!')