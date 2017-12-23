# 12. Write a ship battle game, which is similar to ex.8, except it takes 1 integer as an order of matrix,
#     randomly generates index (x, y) and checks user input (2 integers).
#     (tip: use var1, var2 = raw_input("Enter two numbers here: ").split())
#     *Visualize the game.

def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)
