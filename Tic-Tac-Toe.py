# Tic Tac Toe
# Started at: 11/29/2024
# Finsished at: 

import time
from itertools import cycle

t = 1 # 1 Second

Grid = [["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
        ]

def showGrid():
    print()
    for Row in Grid:
        print(Row)
    print()
    
for i in range(9):
    
    showGrid()
    user1Input = int(input("Choose where to place (x) on the grid (1-9 , 0 = exit): "))
    if user1Input == 1:
        while True:
            if Grid[0][0] == "o" or Grid[0][0] == "x":
                print()
                print("This grid is already taken.")
                time.sleep(t)
                break
            else:
                Grid[0][0] = "x"
                break
    elif user1Input == 2:
        while True:
            if Grid[0][1] == "o" or Grid[0][1] == "x":
                print("This grid is already taken.")
            else:
                Grid[0][1] = "x"
                break
    elif user1Input == 3:
        while True:
            if Grid[0][2] == "o" or Grid[0][2] == "x":
                print("This grid is already taken.")
            else:
                Grid[0][2] = "x"
                break
    elif user1Input == 4:
        while True:
            if Grid[1][0] == "o" or Grid[1][0] == "x":
                print("This grid is already taken.")
            else:
                Grid[1][0] = "x"
                break
    elif user1Input == 5:
        while True:
            if Grid[1][1] == "o" or Grid[1][1] == "x":
                print("This grid is already taken.")
            else:
                Grid[1][1] = "x"
                break
    elif user1Input == 6:
        while True:
            if Grid[1][2] == "o" or Grid[1][2] == "x":
                print("This grid is already taken.")
            else:
                Grid[1][2] = "x"
                break
    elif user1Input == 7:
        while True:
            if Grid[2][0] == "o" or Grid[2][0] == "x":
                print("This grid is already taken.")
            else:
                Grid[2][0] = "x"
                break
    elif user1Input == 8:
        while True:
            if Grid[2][1] == "o" or Grid[2][1] == "x":
                print("This grid is already taken.")
            else:
                Grid[2][1] = "x"
                break
    elif user1Input == 9:
        while True:
            if Grid[2][2] == "o" or Grid[2][2] == "x":
                print("This grid is already taken.")
            else:
                Grid[2][2] = "x"
                break

    showGrid()
    user2Input = int(input("Choose where to place (O) on the grid (1-9 , 0 = exit): "))
    if user2Input == 1:
        while True:
            if Grid[0][0] == "o" or Grid[0][0] == "x":
                print()
                print("This grid is already taken.")
                time.sleep(t)
                break
            else:
                Grid[0][0] = "o"
                break
    elif user2Input == 2:
        while True:
            if Grid[0][1] == "o" or Grid[0][1] == "x":
                print("This grid is already taken.")
            else:
                Grid[0][1] = "o"
                break
    elif user2Input == 3:
        while True:
            if Grid[0][2] == "o" or Grid[0][2] == "x":
                print("This grid is already taken.")
            else:
                Grid[0][2] = "o"
                break
    elif user2Input == 4:
        while True:
            if Grid[1][0] == "o" or Grid[1][0] == "x":
                print("This grid is already taken.")
            else:
                Grid[1][0] = "o"
                break
    elif user2Input == 5:
        while True:
            if Grid[1][1] == "o" or Grid[1][1] == "x":
                print("This grid is already taken.")
            else:
                Grid[1][1] = "o"
                break
    elif user2Input == 6:
        while True:
            if Grid[1][2] == "o" or Grid[1][2] == "x":
                print("This grid is already taken.")
            else:
                Grid[1][2] = "o"
                break
    elif user2Input == 7:
        while True:
            if Grid[2][0] == "o" or Grid[2][0] == "x":
                print("This grid is already taken.")
            else:
                Grid[2][0] = "o"
                break
    elif user2Input == 8:
        while True:
            if Grid[2][1] == "o" or Grid[2][1] == "x":
                print("This grid is already taken.")
            else:
                Grid[2][1] = "o"
                break
    elif user2Input == 9:
        while True:
            if Grid[2][2] == "o" or Grid[2][2] == "x":
                print("This grid is already taken.")
            else:
                Grid[2][2] = "o"
                break