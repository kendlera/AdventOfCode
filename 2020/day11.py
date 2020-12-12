def parseInput():
    with open('input.txt', 'r') as f:
        seats = f.readlines()
    strippedSeats = []
    for s in seats:
        strippedSeats.append(s.strip())
    return strippedSeats

def countOccupiedNeighbors(seatGrid, x, y):
    numOccupied = 0
    maxX = len(seatGrid[0]) - 1
    maxY = len(seatGrid) - 1
    # print("Size now:", maxX, maxY)
    # left
    if x > 0 and seatGrid[y][x-1] == '#':
        numOccupied += 1 
    # left-up diagonal
    if x > 0 and y > 0 and seatGrid[y-1][x-1] == '#':
        numOccupied += 1 
    # up
    if y > 0 and seatGrid[y-1][x] == '#':
        numOccupied += 1
    # right-up diagonal
    if y > 0 and x < maxX and seatGrid[y-1][x+1] == '#':
        numOccupied += 1
    # right
    if x < maxX and seatGrid[y][x+1] == '#':
        numOccupied += 1
    try:
        # right-down diagonal
        if x < maxX and y < maxY and seatGrid[y+1][x+1] == '#':
            numOccupied += 1
    except IndexError:
        print("yo", x, y)
        pass
    # down
    if y < maxY and seatGrid[y+1][x] == '#':
        numOccupied += 1
    # left-down diagonal
    if y < maxY and x > 0 and seatGrid[y+1][x-1] == '#':
        numOccupied += 1
    return numOccupied

def partOne():
    seatGrid = parseInput()
    print("Size:", len(seatGrid[0]), len(seatGrid))
    numChanged = 0
    done = False
    while not done:
        # make a deep copy
        newSeatGrid = [row[:] for row in seatGrid]
        numChanged = 0
        for y in range(len(seatGrid)):
            for x in range(len(seatGrid[y])):
                char = seatGrid[y][x] 
                if char == '.':
                    # empty, nothing to do
                    pass
                elif char == 'L':
                    # empty chair, check if we fill it
                    numOccupied = countOccupiedNeighbors(seatGrid, x, y)
                    if numOccupied is None:
                        return
                    if numOccupied == 0:
                        newRow = newSeatGrid[y]
                        newRow = newRow[:x] + '#' + newRow[x+1:]
                        newSeatGrid[y] = newRow
                        numChanged += 1
                elif char == '#':
                    # occupied chair, check if we empty it
                    numOccupied = countOccupiedNeighbors(seatGrid, x, y)
                    if numOccupied is None:
                        return
                    if numOccupied >= 4:
                        newRow = newSeatGrid[y]
                        newRow = newRow[:x] + 'L' + newRow[x+1:]
                        newSeatGrid[y] = newRow
                        numChanged += 1
        seatGrid = newSeatGrid
        done = (numChanged == 0)
    countOccupied = 0
    for y in range(len(seatGrid)):
        for x in range(len(seatGrid[y])):
            if seatGrid[y][x] == '#':
                countOccupied += 1
    print(countOccupied)

# -----------------------------------------------------

def checkLineOfSight(seatGrid, x, y, slopeX, slopeY):
    inBounds = True
    while inBounds:
        x += slopeX
        y += slopeY
        try:
            if (x < 0 or y < 0):
                return False
            char = seatGrid[y][x]
            if char == '#':
                return True
            elif char == 'L':
                return False
        except IndexError:
            # we've gone off the map without finding a seat
            return False

def countVisibleOccupied(seatGrid, x, y):
    numOccupied = 0
    # left
    if checkLineOfSight(seatGrid, x, y, -1, 0):
        numOccupied += 1 
    # left-up diagonal
    if checkLineOfSight(seatGrid, x, y, -1, -1):
        numOccupied += 1 
    # up
    if checkLineOfSight(seatGrid, x, y, 0, -1):
        numOccupied += 1
    # right-up diagonal
    if checkLineOfSight(seatGrid, x, y, 1, -1):
        numOccupied += 1
    # right
    if checkLineOfSight(seatGrid, x, y, 1, 0):
        numOccupied += 1
    # right-down
    if checkLineOfSight(seatGrid, x, y, 1, 1):
        numOccupied += 1
    # down
    if checkLineOfSight(seatGrid, x, y, 0, 1):
        numOccupied += 1
    # left-down diagonal
    if checkLineOfSight(seatGrid, x, y, -1, 1):
        numOccupied += 1
    return numOccupied

def partTwo():
    seatGrid = parseInput()
    print("Size:", len(seatGrid[0]), len(seatGrid))
    numChanged = 0
    done = False
    while not done:
        # make a deep copy
        newSeatGrid = [row[:] for row in seatGrid]
        numChanged = 0
        for y in range(len(seatGrid)):
            for x in range(len(seatGrid[y])):
                char = seatGrid[y][x] 
                if char == '.':
                    # empty, nothing to do
                    pass
                elif char == 'L':
                    # empty chair, check if we fill it
                    numOccupied = countVisibleOccupied(seatGrid, x, y)
                    if numOccupied is None:
                        return
                    if numOccupied == 0:
                        newRow = newSeatGrid[y]
                        newRow = newRow[:x] + '#' + newRow[x+1:]
                        newSeatGrid[y] = newRow
                        numChanged += 1
                elif char == '#':
                    # occupied chair, check if we empty it
                    numOccupied = countVisibleOccupied(seatGrid, x, y)
                    if numOccupied is None:
                        return
                    if numOccupied >= 5:
                        newRow = newSeatGrid[y]
                        newRow = newRow[:x] + 'L' + newRow[x+1:]
                        newSeatGrid[y] = newRow
                        numChanged += 1
        seatGrid = newSeatGrid
        done = (numChanged == 0)
    countOccupied = 0
    for y in range(len(seatGrid)):
        for x in range(len(seatGrid[y])):
            if seatGrid[y][x] == '#':
                countOccupied += 1
    print(countOccupied)

# partOne()
partTwo()
# 72 is wrong