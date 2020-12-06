def parseInput():
    with open('input.txt', 'r') as f:
        answers = f.read()
    parsed = []
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for ans in answers.split('\n\n'):
        person = ans.split('\n')
        parsedPersons = []
        for p in person:
            resp = '0' * 26 
            for letter in p:
                idx = alpha.index(letter)
                resp = (resp[:idx] + '1' + resp[idx+1:])
            parsedPersons.append(resp)
        parsed.append(parsedPersons)
    return parsed 

def partOne():
    reponses = parseInput() 
    total = 0
    for section in reponses:
        ored = 67108863
        for person in section:
            ored = (ored & int(person, 2))
        oredDec = "{0:b}".format(ored)
        sectionTotal = sum([1 for x in oredDec if x == '1'])
        total += sectionTotal
    print(total)

# partOne()