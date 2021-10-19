numbers = []

with open('input.txt') as file:
    for line in file.readlines():
        numbers.append(int(line))

def getAnswer(sum):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            for k in range(len(numbers)):
                if i != j and j != k and k != i and numbers[i] + numbers[j] + numbers[k] == sum:
                    return numbers[i] * numbers[j] * numbers[k]
    return "Error"

print(getAnswer(2020))