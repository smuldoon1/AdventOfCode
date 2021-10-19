def getAnswerTotal(people):
    answers = []
    for answer in people[0]:
        isAnswerValid = True
        for person in people[1:]:
            if answer in person:
                continue
            isAnswerValid = False
        if isAnswerValid:
            answers.append(answer)
    return len(answers)

total = 0

with open('input.txt') as file:
    groups = file.read().split("\n\n")
    for group in groups:
        people = group.split("\n")
        total += getAnswerTotal(people)
print(total)