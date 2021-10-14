# -*- coding: utf-8 -*-
from main import multiple_two, multiple_three, fizzbuzz
import unittest

class TestCase(unittest.TestCase):

    def test_multiple_two(self):
        self.assertEqual(multiple_two(1), [0])
        self.assertEqual(multiple_two(5), [0, 2, 4])
        self.assertEqual(multiple_two(10), [0, 2, 4, 6, 8, 10])

    def test_multiple_three(self):
        self.assertEqual(multiple_three(1), [0])
        self.assertEqual(multiple_three(5), [0, 3])
        self.assertEqual(multiple_three(10), [0, 3, 6, 9])
        self.assertEqual(multiple_three(12), [0, 3, 6, 9, 12])

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(1), [1])
        self.assertEqual(fizzbuzz(3), [1, 2, 'Fizz'])
        self.assertEqual(fizzbuzz(5), [1, 2, 'Fizz', 4, 'Buzz'])
        self.assertEqual(fizzbuzz(15), [1, 2, 'Fizz', 4, 'Buzz', 'Fizz',
                                        7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz'])


if __name__ == "__main__":
    unittest.main()
