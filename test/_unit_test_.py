import unittest


class TestName(unittest.TestCase):

    def test_name(self):
        name = _name_()
        self.assertEqual(name, 'zhangsan')


def _name_():
    name = input('please input your name!')
    return name


if __name__ == '__main__':
    unittest.main()
