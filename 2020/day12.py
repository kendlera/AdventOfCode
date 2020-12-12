import math

def parseInput():
    with open('input.txt', 'r') as f:
        inst = f.readlines()
    parsedInst = []
    for i in inst:
        char = i[0]
        val = int(i.strip()[1:])
        parsedInst.append([char, val])
    return parsedInst 

def partOne():
    inst = parseInput()
    xVal = 0
    yVal = 0
    direction = 0
    facing = {0: 'E', 90: 'S', 180: 'W', 270: 'N'}
    for i in inst:
        char, val = i
        if char == 'F':
            char = facing[direction]
        if char == 'N':
            yVal += val 
        elif char == 'E':
            xVal += val 
        elif char == 'W':
            xVal -= val 
        elif char == 'S':
            yVal -= val
        elif char == 'R':
            direction = ((direction + val) % 360)
        elif char == 'L':
            direction = ((direction - val) % 360)
    print(abs(xVal) + abs(yVal))

def rotate(point, angle):
    angle = math.radians(0-angle)
    px, py = point

    qx = math.cos(angle) * (px) - math.sin(angle) * (py)
    qy = math.sin(angle) * (px) + math.cos(angle) * (py)
    return [round(qx), round(qy)]

def partTwo():
    inst = parseInput()
    xVal = 0
    yVal = 0
    waypoint = [10, 1]
    for i in inst:
        char, val = i
        if char == 'F':
            for step in range(val):
                x, y = waypoint
                xVal += x 
                yVal += y
        elif char == 'N':
            x, y = waypoint
            waypoint = [x, y+val]
        elif char == 'E':
            x, y = waypoint
            waypoint = [x+val, y]
        elif char == 'W':
            x, y = waypoint
            waypoint = [x - val, y]
        elif char == 'S':
            x, y = waypoint
            waypoint = [x, y-val]
        elif char == 'R':
            waypoint = rotate(waypoint, val)
        elif char == 'L':
            waypoint = rotate(waypoint, 0 - val)
    print(abs(xVal) + abs(yVal))

# print(rotate([10, 4], 90))

partTwo()