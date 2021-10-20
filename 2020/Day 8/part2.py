program = []

with open('input.txt') as file:
    program = file.readlines()

def runProgram(program):
    i = 0
    reg = 0
    visitedIns = []
    while i < len(program):
        if i in visitedIns:
            return False
        visitedIns.append(i)
        ins = program[i][:3]
        val = int(program[i][4:])
        if ins == "acc":
            reg += val
        elif ins == "jmp":
            i += val
            continue
        i += 1
    return reg

flippedJmpNop = -1
while True:
    flippedJmpNop += 1
    alteredProgram = program.copy()
    if alteredProgram[flippedJmpNop][:3] == "jmp":
        alteredProgram[flippedJmpNop] = "nop " + alteredProgram[flippedJmpNop][4:]
    elif alteredProgram[flippedJmpNop][:3] == "nop":
        alteredProgram[flippedJmpNop] = "jmp " + alteredProgram[flippedJmpNop][4:]
    else:
        continue
    returnReg = runProgram(alteredProgram)
    if returnReg != False:
        print(returnReg)
        break