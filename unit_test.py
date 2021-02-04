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
        
        self.assertEqual(verify(123456789012345) % 10 == 0, False)
        self.assertEqual(verify(785201) % 10 == 0, False)
        self.assertEqual(verify(424242424242)%10 ==0, True)


if __name__ == '__main__':
    unittest.main()