import math

instructions = []

with open('input.txt') as file:
    for line in file.readlines():
        instructions.append((line[0], int(line[1:])))

x = y = 0
wpX, wpY = 10, -1

for ins in instructions:
    if ins[0] == 'N':
        wpY -= ins[1]
    elif ins[0] == 'E':
        wpX += ins[1]
    elif ins[0] == 'S':
        wpY += ins[1]
    elif ins[0] == 'W':
        wpX -= ins[1]
    elif ins[0] == 'L':
        tempWpX = round(wpX * math.cos(math.radians(-ins[1])) - wpY * math.sin(math.radians(-ins[1])), 0)
        wpY = round(wpX * math.sin(math.radians(-ins[1])) + wpY * math.cos(math.radians(-ins[1])), 0)
        wpX = tempWpX
    elif ins[0] == 'R':
        tempWpX = round(wpX * math.cos(math.radians(ins[1])) - wpY * math.sin(math.radians(ins[1])), 0)
        wpY = round(wpX * math.sin(math.radians(ins[1])) + wpY * math.cos(math.radians(ins[1])), 0)
        wpX = tempWpX
    elif ins[0] == 'F':
        x += wpX * ins[1]
        y += wpY * ins[1]
print(abs(x) + abs(y))