def parseInput():
    with open('input.txt', 'r') as f:
        passwords = f.readlines()
    parsed = []
    for passw in passwords:
        reqs, password = passw.split(': ')
        counts, req = reqs.split(' ')
        count1, count2 = counts.split('-')
        parsed.append([int(count1), int(count2), req, password])
    return parsed

def partOne():
    options = parseInput()
    validCount = 0
    for option in options:
        c1, c2, let, password = option
        numLetters = 0
        for letter in password:
            if letter == let:
                numLetters += 1
        if numLetters >= c1 and numLetters <= c2:
            validCount += 1

    print(validCount)

def partTwo():
    options = parseInput()
    validCount = 0
    for option in options:
        c1, c2, let, password = option
        val1 = (password[c1 - 1] == let)
        val2 = (password[c2 - 1] == let)
        if val1 != val2:
            validCount += 1

    print(validCount)

