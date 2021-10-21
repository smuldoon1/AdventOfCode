instructions = []

with open('input.txt') as file:
    for line in file.readlines():
        instructions.append((line[0], int(line[1:])))

x = y = 0
dir = 1

for ins in instructions:
    if ins[0] == 'N':
        y -= ins[1]
    elif ins[0] == 'E':
        x += ins[1]
    elif ins[0] == 'S':
        y += ins[1]
    elif ins[0] == 'W':
        x -= ins[1]
    elif ins[0] == 'L':
        dir = (dir - ins[1] / 90) % 4
    elif ins[0] == 'R':
        dir = (dir + ins[1] / 90) % 4
    elif ins[0] == 'F':
        if dir == 0:
            y -= ins[1]
        elif dir == 1:
            x += ins[1]
        elif dir == 2:
            y += ins[1]
        elif dir == 3:
            x -= ins[1]
print(abs(x) + abs(y))