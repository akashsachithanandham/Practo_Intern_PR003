from cchashlib import stringToIntegerArray
from cchashlib import luhnAddition
import sys
import re
from datetime import date

def verify(ccNumber):
    """This function adds up all the digits in a credit card number using Luhn's Addition on one digit out of two.
    
    Arguments:
        ccNumber {string} -- The card number that we want to crunch into a sum.
    
    Returns:
        [integer] -- Sum of the numbers in the credit card. If all 16 digits are entered, it should given a multiple of 10 if the credit card number works.
    """
    #We convert the string that we got in parameter in an array of numbers.
    intArray = []
    intArray = stringToIntegerArray(ccNumber)
    #print(intArray)
    #We initiate the result variable.
    res = 0

    #We iterate on the number array that we got in input.
    for i in range(len(intArray)):

        #If the number is even (knowing that we start counting from the left side of the card number, not the right)
        #We double it and add its digits if needed using luhnAddition
        if(i % 2 == 0):
            res += luhnAddition(intArray[i])

        #If it's not needed, we just let the number like it is and add it to the result.
        else:
            res += intArray[i]

    #We return the result
    res = res%10
    return res==0

def validateName(name):
    exp = r'^[a-zA-Z ]+$'
    if re.search(exp, name):
        return True
    else:
        return False

# helper Function for Number validity


def sum_digits(digit):
    if digit < 10:
        return digit
    else:
        sum = (digit % 10) + (digit // 10)
        return sum

# check number validity
# check cvv validity
def validateCvv(cvv):
    exp = r'\d{3}'
    if re.search(exp, cvv):
        return True
    else:
        return False

# check card Date validatity


def validateExpiry(expiryDate):
    today = date.today()
    todayString = str(today)
    todayMM = todayString[5:7]
    todayYY = todayString[2:4]

    expiryMM = expiryDate[0:2]
    expiryYY = expiryDate[3:]

    expiryYYInt = int(expiryYY)
    expiryMMInt = int(expiryMM)
    todayMMInt = int(todayMM)
    todayYYInt = int(todayYY)

    # print("Today ints", todayMMInt, " ", todayYYInt)
    # print("Expiry ints", expiryMMInt, " ", expiryYYInt)

    if(expiryYYInt < todayYYInt):
        return False
    elif(expiryYY == todayYY):
        if(expiryMMInt < todayMMInt):
            return False
        else:
            return True
    else:
        return True

# checking all details of a card


def checkCardValidity(cardName, cardNumber, cardCvv, cardExpiry):
    cardNumValid = verify(cardNumber)
    cardNameValid = validateName(cardName)
    cardCvvValid = validateCvv(cardCvv)
    cardExpiryValid = validateExpiry(cardExpiry)
    return(cardNameValid and cardNameValid and cardCvvValid and cardExpiryValid)


if __name__ == "__main__":
    cardName = "AkashS"
    cardNumber = "79927398713"
    cardCvv = "388"
    cardExpiry = "07/21"

    print("Card Validation ", checkCardValidity(
        cardName, cardNumber, cardCvv, cardExpiry))