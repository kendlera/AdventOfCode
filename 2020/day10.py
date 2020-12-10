def parseInput():
    with open('input.txt', 'r') as f:
        nums = f.readlines()
    parsedInts = []
    for n in nums:
        parsedInts.append(int(n))
    return parsedInts 

def partOne():
    adapters = parseInput()
    adapters = sorted(adapters)
    num1s = 1
    num3s = 1
    for i in range(len(adapters) - 1):
        diff = adapters[i+1] - adapters[i]
        if (diff == 1):
            num1s += 1
        elif diff == 3:
            num3s += 1
        elif diff > 3:
            print("Difference greater than three", adapters[i], ',', adapters[i+1])
    print(num1s * num3s)

def partTwo():
    adapters = parseInput()
    adapters = sorted(adapters)
    print(adapters)
    # we can break it apart at every 3 diff because that's a required adapter
    adapterChunks = []
    subChunk = []
    for i in range(len(adapters) - 1):
        diff = adapters[i+1] - adapters[i]
        subChunk.append(adapters[i])
        if diff == 2:
            print("2!")
        if diff == 3:
            adapterChunks.append(subChunk)
            subChunk = [] 
    # okay, now we have a list of subchunks 
    print(adapterChunks)
    numCombos = []
    for chunk in adapterChunks:
        if len(chunk) < 3:
            # there are no variations
            numCombos.append(1)
        # we can kinda cheat, knowing that we have chunks of at most length 5
        # the first and last of each chunk we have to keep
        if len(chunk) == 3:
            numCombos.append(2)
        elif len(chunk) == 4:
            numCombos.append(4)
        elif len(chunk) == 5:
            numCombos.append(7) 
    product = 1
    for options in numCombos:
        product = (product * options)
    print(product)

