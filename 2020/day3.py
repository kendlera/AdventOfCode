def parseInput():
    with open('input.txt', 'r') as f:
        treeMap = f.readlines()
    return treeMap

def trajectoryChecker(slopeX, slopeY):
    currX = 0
    currY = 0
    treeMap = parseInput()
    targetY = len(treeMap)
    boundaryX = len(treeMap[0]) - 1
    numTrees = 0
    while currY < targetY:
        if treeMap[currY][currX] == '#':
            numTrees += 1
        currX = ((currX + slopeX) % boundaryX)
        currY += slopeY 
    print(numTrees)
    return numTrees


def partTwo():
    ansA = trajectoryChecker(1, 1)
    ansB = trajectoryChecker(3, 1)
    ansC = trajectoryChecker(5, 1)
    ansD = trajectoryChecker(7, 1)
    ansE = trajectoryChecker(1, 2)
    print(ansA * ansB * ansC * ansD * ansE)
