buses = []
initialTime = -1
with open('input.txt') as file:
    initialTime = int(file.readline())
    for bus in file.readline().replace(",x", "").split(','):
        buses.append(int(bus))

minimumWait = 999999999999
busID = -1
for bus in buses:
    wait = bus - (initialTime % bus)
    if wait < minimumWait:
        minimumWait = wait
        busID = bus
print(busID * minimumWait)