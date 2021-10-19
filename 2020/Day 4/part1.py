import re

passports = []

with open('input.txt') as file:
    passports = file.read().split("\n\n")

validPassports = 0
for passport in passports:
    checks = 0
    for data in re.split(' |\n', passport):
        f = data[0:3]
        if f == "byr" or f == "iyr" or f == "eyr" or f == "hgt" or f == "hcl" or f == "ecl" or f == "pid":
            checks += 1
    if checks >= 7:
        validPassports += 1
print(validPassports)