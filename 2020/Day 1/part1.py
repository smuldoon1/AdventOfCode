numbers = []

with open('input.txt') as file:
    for line in file.readlines():
        numbers.append(int(line))

def getAnswer(sum):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j and numbers[i] + numbers[j] == sum:
                return numbers[i] * numbers[j]
    return "Error"

print(getAnswer(2020))