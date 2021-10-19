treemap = []

with open('input.txt') as file:
    treemap = file.readlines()

x = y = treeCount = 0
while y < len(treemap):
    if treemap[y][x] == '#':
        treeCount += 1
    x = (x + 3) % 31
    y += 1
print(treeCount)