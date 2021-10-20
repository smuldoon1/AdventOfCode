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

print(numbers[i])