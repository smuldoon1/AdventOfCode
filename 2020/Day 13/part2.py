buses = []
offsets = []
initialTime = -1
with open('test.txt') as file:
    initialTime = int(file.readline())
    i = 0
    for bus in file.readline().split(','):
        if bus != 'x':
            buses.append(int(bus))
            offsets.append(i)
        i += 1
print(buses)
print(offsets)
time = buses[0]
inc = buses[0]
i = 0
while True:
    while i < len(buses):
        print(str(buses[i]) + ": " + str((time + offsets[i]) % buses[i]))
        if (time + offsets[i]) % buses[i] == 0:
            inc = time
            i += 1
            time = 0
        else:
            break
    time += inc
    print(time, inc)
    input("")
    