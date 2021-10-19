import re

passports = []

def checkHeight(field):
    unit = field[len(field) - 2:]
    if unit == "cm":
        height = int(field[0:len(field) - 2])
        return height >= 150 and height <= 193
    elif unit == "in":
        height = int(field[0:len(field) - 2])
        return height >= 59 and height <= 76
    return False

def checkHairColour(field):
    return field[0] == '#' and len(field) == 7 and int(field[1:], 16)

def checkEyeColour(field):
    return field == "amb" or field == "blu" or field == "brn" or field == "gry" or field == "grn" or field == "hzl" or field == "oth"

with open('input.txt') as file:
    passports = file.read().split("\n\n")

validPassports = 0
for passport in passports:
    checks = 0
    for data in re.split(' |\n', passport):
        field = data.strip().split(":")
        if ((field[0] == "byr" and int(field[1]) >= 1920 and int(field[1]) <= 2002) or
            (field[0] == "iyr" and int(field[1]) >= 2010 and int(field[1]) <= 2020) or
            (field[0] == "eyr" and int(field[1]) >= 2020 and int(field[1]) <= 2030) or
            (field[0] == "hgt" and checkHeight(field[1])) or
            (field[0] == "hcl" and checkHairColour(field[1])) or
            (field[0] == "ecl" and checkEyeColour(field[1])) or
            (field[0] == "pid" and len(field[1]) == 9 and field[1].isdigit())
        ):
            checks += 1
    if checks >= 7:
        validPassports += 1
print(validPassports)