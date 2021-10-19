import math

highestSeatValue = -1

with open('input.txt') as file:
    for line in file.readlines():
        rowMin, rowMax, colMin, colMax = 0, 127, 0, 7
        for i in range(7):
            if line[i] == 'F':
                rowMax -= math.ceil((rowMax - rowMin) * .5)
            if line[i] == 'B':
                rowMin += math.ceil((rowMax - rowMin) * .5)
        for i in range(7, 10):
            if line[i] == 'L':
                colMax -= math.ceil((colMax - colMin) * .5)
            if line[i] == 'R':
                colMin += math.ceil((colMax - colMin) * .5)
        seatID = rowMin * 8 + colMin
        if seatID > highestSeatValue:
            highestSeatValue = seatID
print(highestSeatValue)