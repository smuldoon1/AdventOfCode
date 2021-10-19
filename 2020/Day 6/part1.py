total = 0

with open('input.txt') as file:
    groups = file.read().split("\n\n")
    for group in groups:
        answers = []
        for answer in group:
            if answer.isalpha() and answer not in answers:
                answers.append(answer)
        total += len(answers)
print(total)