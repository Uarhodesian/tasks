# 5. Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:
# ****
# *********
# ******
def histogram(numList):
        for i in numList:
                ch = "*"
                print(i*ch)

