memoryDict = {}
mask = ""

def maskValue(value):
    for i in range(0, 36):
        if mask[i] == '1':
            value |= 1 << (i)
    return value

with open('test.txt') as file:
    for line in file.readlines():
        if line[0:4] == "mask":
            mask = line[7:]
            print(mask)
        else:
            splitLine = line.split(']')
            print(bin(int(splitLine[1][3:])))
            memoryDict[splitLine[0][4:]] = maskValue(int(splitLine[1][3:]))
            print(bin(memoryDict[splitLine[0][4:]]))
