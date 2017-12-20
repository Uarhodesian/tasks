# 12. Write a ship battle game, which is similar to ex.8, except it takes 1 integer as an order of matrix,
#     randomly generates index (x, y) and checks user input (2 integers).
#     (tip: use var1, var2 = raw_input("Enter two numbers here: ").split())
#     *Visualize the game.

import random

def battle_ship():
    board = []
    for i in range(5):
        board.append(["0"] * 5)
    print (board)
