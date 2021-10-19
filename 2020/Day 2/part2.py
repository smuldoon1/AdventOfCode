import re

def isPasswordValid(p1, p2, letter, password):
    if (password[p1 - 1] == letter) != (password[p2 - 1] == letter):
        return True
    return False

with open('input.txt') as file:
    validPasswords = 0
    for line in file.readlines():
        s = re.split('-|:| ', line)
        if isPasswordValid(int(s[0]), int(s[1]), s[2], s[4]):
            validPasswords += 1
    print(validPasswords)