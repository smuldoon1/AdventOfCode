incrementCount = 0

with open('input.txt') as file:
    numbers = file.readlines()
    previousWindow = int(numbers[0]) + int(numbers[1]) + int(numbers[2])
    for i in range(3, len(numbers)):
        currentWindow = int(numbers[i]) + int(numbers[i-1]) + int(numbers[i-2])
        if currentWindow > previousWindow:
            incrementCount += 1
        previousWindow = currentWindow

print(incrementCount)