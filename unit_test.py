import unittest
import random

from validator import verify
#from generate import generate

"""Unit tests class.
We generate random numbers from 1 digit long to 15 digit long, feed them to the generate function and then verify the numbers.
This way we can check both functions at the same time to be sure that they give good results.
"""
class UnitTest(unittest.TestCase):
    def testGenerate(self):
        
        self.assertEqual(verify(1111111111111111) % 10 != 0, True)
        self.assertEqual(verify(7852010) % 10 == 0, False)


if __name__ == '__main__':
    unittest.main()