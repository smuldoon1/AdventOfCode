import math

seats = []

with open('input.txt') as file:
    seats = file.readlines()

def isNeighbourOccupied(row, column, xInc, yInc, seatArray):
    y = row + yInc
    x = column + xInc
    while x >= 0 and y >= 0 and x < len(seatArray[0]) - 1 and y < len(seatArray):
        if seatArray[y][x] == '.':
            y += yInc
            x += xInc
            continue
        elif seatArray[y][x] == '#':
            return 1
        break
    return 0

def setSeat(row, column, seatArray):
    adjacentOccupied = 0
    if seatArray[row][column] == '.':
        return None
    for r in range(-1, 2):
        for c in range(-1, 2):
            if (r != 0 or c != 0):
                adjacentOccupied += isNeighbourOccupied(row, column, c, r, seatArray)
    if seatArray[row][column] == 'L' and adjacentOccupied == 0:
        return '#'
    elif seatArray[row][column] == '#' and adjacentOccupied >= 5:
        return 'L'
    return None

hasChanged = True
while hasChanged:
    hasChanged = False
    newSeats = seats.copy()
    for r in range(len(seats)):
        newRow = ""
        for c in range(len(seats[r])):
            seatChange = setSeat(r, c, seats)
            if seatChange != None:
                newRow += seatChange
                hasChanged = True
            else:
                newRow += seats[r][c]
        newSeats[r] = newRow
    seats = newSeats

occupiedSeats = 0
for r in range(len(seats)):
    for c in range(len(seats[r])):
        if seats[r][c] == '#':
            occupiedSeats += 1
print(occupiedSeats)