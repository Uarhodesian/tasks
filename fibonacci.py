# 12. Write a ship battle game, which is similar to ex.8, except it takes 1 integer as an order of matrix,
#     randomly generates index (x, y) and checks user input (2 integers).
#     (tip: use var1, var2 = raw_input("Enter two numbers here: ").split())
#     *Visualize the game.

def recur_fibo(n):
   """Recursive function to
   print Fibonacci sequence"""
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

# Change this value for a different result
nterms = 10

# uncomment to take input from the user
#nterms = int(input("How many terms? "))

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))
