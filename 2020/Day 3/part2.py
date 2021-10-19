treemap = []

with open('input.txt') as file:
    treemap = file.readlines()

def getTreesInSlope(xInc, yInc):
    x = y = treeCount = 0
    while y < len(treemap):
        if treemap[y][x] == '#':
            treeCount += 1
        x = (x + xInc) % 31
        y += yInc
    return treeCount

print(getTreesInSlope(1, 1) * getTreesInSlope(3, 1) * getTreesInSlope(5, 1) * getTreesInSlope(7, 1) * getTreesInSlope(1, 2))