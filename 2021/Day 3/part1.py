with open('input.txt') as file:
    gamma = ""
    epsilon = ""
    lines = file.readlines()
    for i in range(len(lines[0]) - 1):
        ones = 0
        for line in lines:
            if line[i] == '1':
                ones += 1
        if ones > len(lines) * 0.5:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    print(int(gamma, 2) * int(epsilon, 2))