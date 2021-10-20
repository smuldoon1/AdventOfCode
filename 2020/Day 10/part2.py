adapters = [0]

with open('test.txt') as file:
    for adapter in file.readlines():
        adapters.append(int(adapter))
    adapters.sort()
    adapters.append(adapters[len(adapters) - 1] + 3)

diffs = []
for i in range(len(adapters) - 1):
    diffs.append(adapters[i + 1] - adapters[i])

print(diffs)