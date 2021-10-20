adapters = [0]

with open('input.txt') as file:
    for adapter in file.readlines():
        adapters.append(int(adapter))
    adapters.sort()

diff1s = 0
diff3s = 1
for i in range(len(adapters) - 1):
    if adapters[i + 1] - adapters[i] == 1:
        diff1s += 1
    else:
        diff3s += 1
print(diff1s * diff3s)