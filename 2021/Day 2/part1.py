x, y = 0, 0

with open('input.txt') as file:
    for line in file.readlines():
        ins = line.split(" ")
        if ins[0] == "forward":
            x += int(ins[1])
        elif ins[0] == "up":
            y -= int(ins[1])
        elif ins[0] == "down":
            y += int(ins[1])

print(x * y)
