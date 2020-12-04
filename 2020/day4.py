import json

def parseInput():
    with open('input.txt', 'r') as f:
        passportInfo = f.read()
    sepPassports = passportInfo.split('\n\n')
    parsedPassports = []
    for passP in sepPassports:
        parsed = passP.replace('\n', ',')
        parsed = parsed.replace(' ', ',')
        parsed = parsed.split(',')
        allAttrs = []
        for elem in parsed:
            allAttrs.append(elem.split(':'))
        parsedPassports.append(allAttrs)
    return parsedPassports


def partOne():
    passports = parseInput()
    numValid = 0
    validReqs = ['byr','iyr','eyr','hgt','hcl','ecl','pid' ]
    for elem in passports:
        foundAllReqs = True
        for req in validReqs:
            foundReq = False
            for attr in elem:
                if attr[0] == req:
                    validValue = globals()[attr[0]](attr[1])
                    if validValue:
                        foundReq = True
                    break
            if not foundReq:
                foundAllReqs = False 
                break;
        if foundAllReqs:
            numValid += 1
    print(numValid)


def byr(value):
    if len(value) != 4:
        return False
    val = int(value)
    return (val >= 1920 and val <= 2002)

def iyr(value):
    if len(value) != 4:
        return False
    val = int(value)
    return (val >= 2010 and val <= 2020)

def eyr(value):
    if len(value) != 4:
        return False
    val = int(value)
    return (val >= 2020 and val <= 2030)

def hgt(value):
    numLen = len(value) - 2
    try:
        val = int(value[:numLen])
    except ValueError:
        return False
    metric = value[-2:]
    if metric == 'in':
        return val >= 59 and val <= 76
    elif metric == 'cm':
        return val >= 150 and val <= 193
    return False 

def hcl(value):
    if len(value) != 7:
        return False
    if value[0] != '#':
        return False 
    try:
        int(value[1:], 16)
    except ValueError:
        return False 
    return True 

def ecl(value):
    valid = ['amb','blu','brn','gry','grn','hzl','oth']
    return value in valid 

def pid(value):
    try:
        int(value)
    except ValueError:
        return False
    return len(value) == 9
