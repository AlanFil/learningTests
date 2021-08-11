import unittest
from fractions import Fraction


def func_for_tests(numbers):
    return sum(numbers)


class Test(unittest.TestCase):
    def test_func1_sum(self):
        self.assertEqual(func_for_tests([1, 2, 3]), 6)

    def test_func1_is_not_none(self):
        self.assertIsNotNone(func_for_tests([1, 2, 3]))

    def test_fractions(self):
        self.assertEqual(func_for_tests([Fraction(1, 4), Fraction(1, 4), Fraction(1, 2)]), 1)

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            func_for_tests('dupa')


if __name__ == '__main__':
    unittest.main()
