from typing import Union
import unittest
from unittest.main import main
from calculator import calculator

class TestCal(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(calculator.sum(1,1), 2)

    def test_sub(self):
        self.assertEqual(calculator.sub(1,2), -1)
    
    def test_mul(self):
        self.assertEqual(calculator.mul(1,2), 2)

    def test_div(self):
        self.assertEqual(calculator.div(2,1), 2)

if __name__ == "__main__":
    unittest.main()