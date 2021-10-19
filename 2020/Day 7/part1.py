import re

bags = {}

with open('input.txt') as file:
    lines = file.readlines()
    for line in lines:
        parsedLine = re.split(" contain |, ", line.replace(" bags", "").replace(" bag", "").replace(".\n", ""))
        bags[parsedLine[0]] = []
        for i in range(1, len(parsedLine)):
            bags[parsedLine[0]].append(parsedLine[i][2:])

validBags = ["shiny gold"]
i = 0
while i < len(validBags):
    for bag in bags:
        if validBags[i] in bags[bag]:
            if bag not in validBags:
                validBags.append(bag)
    i += 1
print(len(validBags) - 1)