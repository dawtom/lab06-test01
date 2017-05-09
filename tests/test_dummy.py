import unittest

from eternal.main import calculate, main

"""
Run with PYTHONPATH=. python tests/test_dummy.py
"""


class TestDummy(unittest.TestCase):

    def test_fun(self):
        weekday = calculate(2004, 2, 29)
        self.assertEqual(weekday, 7)

        with self.assertRaises(Exception):
            calculate(1900, 2, 29)
        with self.assertRaises(Exception):
            calculate(178, 255, 29)
        with self.assertRaises(Exception):
            calculate(1900, 2, 293)
        with self.assertRaises(Exception):
            calculate(2017, 32, 0)

        weekday = calculate(1791, 5, 3)
        self.assertEqual(weekday, 2)




        retcode = main(("--year", "2001", "--month", "1", "--day", "3"))
        self.assertEqual(retcode, 0)

        with self.assertRaises(Exception):
            main(("--year", 555555, "--month", 5))


if __name__ == '__main__':
    unittest.main()
