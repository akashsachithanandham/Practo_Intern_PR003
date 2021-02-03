import sys

def stringToIntegerArray(inputString):
    """This function is used to transform a string array (the one we get as an argument) into an integer array
    
    Arguments:
        inputString {string} -- The input string that will be converted in an integer array
    
    Returns:
        array<integer> -- The integer array converted from the string
    """
    res = []
    #For each character in our input array, we get the character, transform it into an integer and remove 48
    #which is the offset for numbers in the ASCII table.
    inputString = str(inputString)
    for i in range(len(inputString)) :
        res.append(ord(inputString[i]) - 48)
    return res

def checkNumberIntegrity(string):
    """This function allows us to check if a credit card number given is valid or not
    
    Arguments:
        string {string} -- The credit card number given in argument
    
    Returns:
        [ -- [description]
    """

    #If the input given is not 16 numbers long, we throw an exception.
    if len(string) != 16 :
        Exception("The credit card number you put is not 16 numbers long, it's only " + str(len(string)))

    #This line allows us to check every character of the string given and see if this is a number or not. If it's not, we throw an exception.
    map(Exception('The credit card number you put is invalid !'), filter(str.isdigit, string))


def luhnAddition(inputInt):
    """This function takes in an integer and doubles it. If the result is equal or greater than 10, it adds up the digits.
    
    Arguments:
        inputInt {integer} -- This is the integer to be doubled by the function.
    
    Returns:
        integer -- Gives the transformed integer
    """
    #If the number is greater than 4, doubling it will give a result equal or greater than 10 so we add the digits
    if(inputInt > 4):
        return 1 + (inputInt*2 % 10)
    #If it's not, we double it normally and send it back
    else:
        return inputInt * 2