import unittest
import random

from validator import verify
from validator import validateCvv
from validator import validateName
from validator import validateExpiry
from validator import checkCardValidity
#from generate import generate

"""Unit tests class.
We generate random numbers from 1 digit long to 15 digit long, feed them to the generate function and then verify the numbers.
This way we can check both functions at the same time to be sure that they give good results.
"""
class UnitTest(unittest.TestCase):
    def testGenerate(self):
        
        self.assertEqual(verify(123456789012345), False)
        self.assertEqual(verify(785201), False)
        self.assertEqual(verify(424242424242), True)

    def testValidateCvv(self):
        print(validateCvv("1678797887"))
        assert validateCvv("314") == True
        assert validateCvv("615") == True
        assert validateCvv("-91") == False
        assert validateCvv("1678797887") == False


    def testValidateName(self):
        assert validateName("Akash") == True
        assert validateName("Balaji") == True
        assert validateName("8965555") == False
       


    def testValidateExpiry(self):
        assert validateExpiry("07/22") == True
        assert validateExpiry("08/30") == True
        assert validateExpiry("89/11") == False
        
    def testCheckCardValidity(self):
        assert checkCardValidity(
            "Akash", "79927398713", "343", "03/22") == True
        assert checkCardValidity(
            "Sanjay", "79927391134", "51", "04/23") == False
        assert checkCardValidity(
            "Buvan", "79927391134", "113", "03/27") == True
        
if __name__ == '__main__':
    unittest.main()