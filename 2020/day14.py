def parseInput():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    parsedLines = []
    for l in lines:
        a, b = l.strip().split(' = ')
        if a == 'mask':
            parsedLines.append([a, b])
        else:
            addr = int(a[4:-1])
            val = int(b)
            parsedLines.append([addr, val])
    return parsedLines

def partOne():
    lines = parseInput()
    memory = {}
    andMask = ''
    orMask = ''
    for l in lines:
        a, b = l
        if a == 'mask':
            andMask = int(b.replace('X', '1'), 2)
            orMask = int(b.replace('X', '0'), 2)
        else:
            val = (b & andMask)
            val = (val | orMask)
            memory[a] = val
    total = 0
    for m in memory:
        total += memory[m]
    print(total)

# partOne()

def getFluxValues(val):
    numXs = val.count('X')
    maxVal = int('1' * numXs, 2)
    fluxVals = []
    for v in range(maxVal+1):
        temp = val 
        repl = bin(v).replace("0b", "").zfill(numXs)
        for i in range(len(temp)):
            if temp[i] == 'X':
                temp = temp[:i] + repl[0] + temp[i+1:]
                repl = repl[1:]
        fluxVals.append(int(temp, 2))
    return fluxVals

def partTwo():
    lines = parseInput()
    memory = {}
    orMask = ''
    xMask = ''
    for line in lines:
        a, b = line 
        if a == 'mask':
            orMask = int(b.replace('X', '0'), 2)
            xMask = b
        else:
            mem = bin(a | orMask).replace("0b", "").zfill(36)
            for i in range(len(xMask)):
                if xMask[i] == 'X':
                    mem = mem[:i] + 'X' + mem[i+1:]
            memVals = getFluxValues(mem)
            for m in memVals:
                memory[m] = b
    total = 0
    for m in memory:
        total += memory[m]
    print(total)

# print(getFluxValues('XXX'))

partTwo()