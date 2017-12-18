# 11. Write a function dec_to_bin() that takes decimal integer and outputs its binary representation.

def dec_to_bin(n):
   """Function to print binary number
   for the input decimal using recursion"""
   if n > 1:
       dec_to_bin(n//2)
   print(n % 2,end = '')


