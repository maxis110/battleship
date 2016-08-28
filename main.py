import random

def startGame(ship_quant, size):
    counts = 0
    attempts = []
    field = genField(size)
    ship = createShip(ship_quant, field)
    while ship:
        if counts < (size*size - ship_quant) :
            shot = []
            row = int(raw_input("Select row:"))
            shot.append(row)
            col = int(raw_input("Select colunm:"))
            shot.append(col)
            if col < len(field) and row < len(field):
                if shot not in attempts:
                    attempts.append(shot)
                    if shot in ship:
                        ship.remove(shot)
                        print ship
                        print('Ship founded:',shot)
                    else:
                        counts += 1
                        field[row][col] = 'X'
                        for i in range(len(field)):
                            print ' '.join(str(rows) for rows in field[i])
                else:
                    print('bomb already there')
            else:
                print('out of playboard')
        else:
            print('game over')
            break
def createShip(quantity, field):
    fleet = []
    while quantity:
        ship = []
        ship_row = random.randrange(0, len(field), 1)
        ship.append(ship_row)
        ship_column = random.randrange(0, len(field), 1)
        ship.append(ship_column)
        if ship not in fleet:
            fleet.append(ship)
            quantity -= 1
    print ('random ship on: ',fleet)
    return fleet

def genField(size):
    field=[]
    [field.append(['0']*size) for elem in range(size)]
    return field

startGame(6,3)
