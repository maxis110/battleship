
from __future__ import print_function
import random

def startGame(counts, ship_quant, field_row, field_col):
    attempts = []
    field = genField(field_row,field_col)
    ship = createShip(ship_quant)
    ship_row = ship[0][0]
    ship_col = ship[0][1]
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

def createShip(quantity):
    fleet = []
    for elem in range(quantity):
        ship = []
        ship_row = random.randrange(0, 2, 1)
        ship.append(ship_row)
        ship_column = random.randrange(0, 2, 1)
        ship.append(ship_column)
        if ship not in fleet:
            fleet.append(ship)
    print(fleet)
    return fleet

def genField(rows, columns):
    field = []
    for elem in range(rows):
        field.append([])
        for j in range(columns):
            field[elem].append(0)
    return (field)

startGame(8,1,3,3)