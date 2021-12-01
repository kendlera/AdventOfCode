import copy

def parseInput():
    with open('input.txt', 'r') as f:
        grid = f.readlines()
    collen = len(grid[0].strip()) + 16
    rowlen = len(grid) + 16
    zlen = 8
    emptyRow = '.' * collen
    fullGrid = []
    for g in range(zlen):
        elems = []
        for x in range(rowlen):
            elems.append(emptyRow)
        fullGrid.append(elems)
    elems = []
    for x in range(8):
        elems.append(emptyRow)
    for g in grid:
        myRow = ('.' * 8) + g.strip() + ('.' * 8)
        elems.append(myRow)
    for x in range(8):
        elems.append(emptyRow)
    fullGrid.append(elems)
    for g in range(zlen):
        elems = []
        for x in range(rowlen):
            elems.append(emptyRow)
        fullGrid.append(elems)
    return fullGrid

def countNeighbors(grid, x, y, z):
    xmin = max(x-1, 0)
    ymin = max(y-1, 0)
    zmin = max(z-1, 0)
    numActive = 0
    for zIdx in range(zmin, z + 1):
        for yIdx in range(ymin, y + 1):
            for xIdx in range(xmin, x + 1):
                if x == xIdx and y == yIdx and z == zIdx:
                    continue
                try:
                    elem = grid[zIdx][yIdx][xIdx]
                except IndexError:
                    continue
                if elem == '#':
                    numActive += 1
    return numActive

def partOne():
    # headache
    grid = parseInput()
    zRange = len(grid)
    yRange = len(grid[0])
    xRange = len(grid[0][0])
    for bootCycle in range(6):
        newGrid = copy.deepcopy(grid)
        for z in range(zRange):
            for y in range(yRange):
                for x in range(xRange):
                    elem = grid[z][y][x]
                    active = (elem == '#')
                    numNeighbors = countNeighbors(grid, x, y, z)
                    if active and numNeighbors != 2 and numNeighbors != 3:
                        # make this inactive
                        newRow = grid[z][y][:x] + '.' + grid[z][y][x+1:]
                        newGrid[z][y] = newRow
                    elif not active and numNeighbors == 3:
                        # make this active
                        newRow = grid[z][y][:x] + '#' + grid[z][y][x+1:]
                        newGrid[z][y] = newRow
        grid = newGrid
    # all booted up, now count the active
    numActive = 0
    for z in range(zRange):
        for y in range(yRange):
            for x in range(xRange):
                if grid[z][y][x] == '#':
                    numActive += 1
    print(numActive)

partOne()

# 8 is wrong
