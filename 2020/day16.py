def parseInput():
    with open('input.txt', 'r') as f:
        tickets = f.readlines()
    parsedTickets = []
    for t in tickets:
        parsed = []
        for elem in t.strip().split(','):
            parsed.append(int(elem))
        parsedTickets.append(parsed)
    validValues = {'departure location': [[44,401], [415,965]],
                    'departure station': [[44,221], [243,953]],
                    'departure platform': [[29, 477], [484, 963]],
                    'departure track': [[43, 110], [126, 951]],
                    'departure date': [[48, 572], [588, 965]],
                    'departure time': [[48, 702], [719, 955]],
                    'arrival location': [[35, 336], [358,960]],
                    'arrival station': [[47, 442], [449, 955]],
                    'arrival platform': [[25, 632], [639, 970]],
                    'arrival track': [[34, 461], [472, 967]],
                    'class': [[41, 211], [217, 959]],
                    'duration': [[29, 500], [519, 969]],
                    'price': [[39, 423], [440, 969]],
                    'route': [[50, 264], [282, 958]],
                    'row': [[50, 907], [920, 972]],
                    'seat': [[27, 294], [315, 954]],
                    'train': [[29, 813], [827, 962]],
                    'type': [[45, 531], [546, 956]],
                    'wagon': [[29, 283], [292, 957]],
                    'zone': [[45, 518], [525, 974]] }
    return parsedTickets, validValues

'''
def consolidateValidValues(rules):
    validValues = [[44,401], [415,965]]
    for rule in rules:
        for validRange in rules[rule]:
            a, b = validRange
            for run in validValues:
                c, d = run 
                # the range is before the first element
                if b < (c - 1):
'''

def partOne():
    tickets, rules = parseInput()
    countInvalid = 0
    validTickets = []
    for ticket in tickets:
        invalid = False
        for ticketVal in ticket:
            inRange = False
            for rule in rules:
                for valRange in rules[rule]:
                    start, stop = valRange
                    if ticketVal >= start and ticketVal <= stop:
                        inRange = True
                        break;
                if inRange:
                    break
            if not inRange:
                countInvalid += ticketVal
                invalid = True
        if not invalid:
            validTickets.append(ticket)
    # print(validTickets)
    print(countInvalid)
    return validTickets

def partTwo():
    tickets, rules = parseInput()
    validTickets = partOne()
    positions = len(validTickets[0])
    contenders = {}
    for i in range(positions):
        contenders[i] = list(rules.keys())
    for ticket in validTickets:
        for pos in range(len(ticket)):
            options = contenders[pos]
            toRemove = []
            value = ticket[pos]
            if len(options) == 1:
                continue
            for op in options:
                rejected = True
                for valRange in rules[op]:
                    start, stop = valRange
                    if value >= start and value <= stop:
                        rejected = False
                        break
                if rejected:
                    toRemove.append(op)
            remaining = [op for op in options if op not in toRemove]
            contenders[pos] = remaining
    print(contenders)

{0: ['arrival station'], 
1: ['row'], 
2: ['wagon'], 
3: ['arrival location'], 
4: ['type'], 
5: ['route'], 
6: ['departure date'], 
7: ['zone'], 
8: ['arrival track'], 
9: ['seat'], 
10: ['departure location'], 
11: ['departure time'], 
12: ['departure platform'], 
13: ['arrival platform'], 
14: ['price'], 
15: ['departure track'], 
16: ['duration'], 
17: ['departure station'], 
18: ['class'], 
19: ['train']}