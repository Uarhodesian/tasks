# Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.
def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum

def listmult(numList):
    theMult = 1
    for i in numList:
        theMult = theMult * i
    return theMult
