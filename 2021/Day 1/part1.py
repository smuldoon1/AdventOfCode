incrementCount = 0

with open('input.txt') as file:
    numbers = file.readlines()
    previousNumber = int(numbers[0])
    for i in range(1, len(numbers)):
        if int(numbers[i]) > previousNumber:
            incrementCount += 1
        previousNumber = int(numbers[i])

print(incrementCount)