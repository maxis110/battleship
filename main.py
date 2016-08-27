
from __future__ import print_function
import random

def startGame(counts):
    attempts = []
    field = genField()
    ship = createShip()
    ship_row = ship[0]
    ship_col = ship[1]
    while counts:
        try:
            shot = []
            row = int(raw_input("Select row:"))
            shot.append(row)
            col = int(raw_input("Select colunm:"))
            shot.append(col)
            counts -= 1
            if shot not in attempts:
                attempts.append(shot)
                if row == ship_row and col == ship_col:
                    print('Ship founded:',ship_row, ship_col)
                    break
                else:
                    field[row][col] = 'X'
                    for i in range(len(field)):
                        for j in range(len(field[i])):
                            print (field[i][j],end = ' ')
                        print ()
            else:
                print('bomb already there')
        except:
            print('shot outside the play field')

def createShip():
    ship_row =  random.randrange(0, 2, 1)
    ship_column = random.randrange(0, 2, 1)
    print(ship_row, ship_column)
    return ship_row, ship_column

def genField():
    field = []
    for elem in range(0,3):
        field.append([])
        for j in range(0,3):
            field[elem].append(0)
    return field

startGame(8)