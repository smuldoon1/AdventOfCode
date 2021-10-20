import math

seats = []

with open('input.txt') as file:
    seats = file.readlines()

def setSeat(row, column, seatArray):
    adjacentOccupied = 0
    for r in range(max(0, row - 1), min(len(seatArray), row + 2)):
        for c in range(max(0, column - 1), min(len(seatArray[r]), column + 2)):
            if (r != row or c != column) and seatArray[r][c] == '#':
                adjacentOccupied += 1
    if seatArray[row][column] == 'L' and adjacentOccupied == 0:
        return '#'
    elif seatArray[row][column] == '#' and adjacentOccupied >= 4:
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