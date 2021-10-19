import re

def isPasswordValid(minL, maxL, letter, password):
    count = 0
    for c in password:
        if c == letter:
            count += 1
    if count < minL or count > maxL:
        return False
    return True

with open('input.txt') as file:
    validPasswords = 0
    for line in file.readlines():
        s = re.split('-|:| ', line)
        if isPasswordValid(int(s[0]), int(s[1]), s[2], s[4]):
            validPasswords += 1
    print(validPasswords)