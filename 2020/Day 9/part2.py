import math

numbers = []

with open('input.txt') as file:
    for number in file.readlines():
        numbers.append(int(number))

def isValid(i):
    for a in numbers[i-25:i]:
        for b in numbers[i-25:i]:
            if a + b == numbers[i] and a != b:
                return True
    return False

i = 25
while True:
    if not isValid(i):
        break
    i += 1

answerIndex = i
numberRange = 2
sumFound = False
while not sumFound:
    for i in range(answerIndex - numberRange):
        sum = 0
        minNumber = 99999999999999
        maxNumber = -99999999999999
        for numberIndex in range(i, i + numberRange):
            sum += numbers[numberIndex]
            minNumber = min(minNumber, numbers[numberIndex])
            maxNumber = max(maxNumber, numbers[numberIndex])
        if sum == numbers[answerIndex]:
            print(minNumber + maxNumber)
            sumFound = True
            break
    numberRange += 1