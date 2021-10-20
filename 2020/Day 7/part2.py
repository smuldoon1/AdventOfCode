import re

bags = {}

with open('input.txt') as file:
    lines = file.readlines()
    for line in lines:
        parsedLine = re.split(" contain |, ", line.replace("no other bags.", "0").replace(" bags", "").replace(" bag", "").replace(".\n", ""))
        bags[parsedLine[0]] = []
        for i in range(1, len(parsedLine)):
            bags[parsedLine[0]].append([parsedLine[i][2:], int(parsedLine[i][0])])

bagsToCheck = ["shiny gold"]
total = 0
while len(bagsToCheck) > 0:
    for containedBag in bags[bagsToCheck[0]]:
        for amount in range(containedBag[1]):
            bagsToCheck.append(containedBag[0])
            total += 1
    bagsToCheck.pop(0)
print(total)