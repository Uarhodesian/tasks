# 8. Write a function game() number-guessing game, that takes 2 int parameters defining the range.
#    Using random.randint(A, B) generate random int from the range.
#    While user input isn't equal that number, print "Try again!". If user guess the number, congratulate him and exit. (use raw_input())

import random
def game():
    you1 = int(input("Enter first number from 1 to 6: "))
    you2 = int(input("Enter second number from 1 to 6: "))
    comp1 = random.randint(1,6) 
    comp2 = random.randint(1,6)
    print("your turn", you1,you2)
    print("comp turn", comp1,comp2)
    if you1 == comp1 and you2 == comp2:
        print("Congrat, buddy - you won!")
    else:
        print("Try again, buddy!")
