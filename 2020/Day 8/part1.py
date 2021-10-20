program = []

with open('input.txt') as file:
    program = file.readlines()

i = 0
reg = 0
visitedIns = []
while i < len(program):
    if i in visitedIns:
        break
    visitedIns.append(i)
    ins = program[i][:3]
    val = int(program[i][4:])
    if ins == "acc":
        reg += val
    elif ins == "jmp":
        i += val
        continue
    i += 1
print(reg)