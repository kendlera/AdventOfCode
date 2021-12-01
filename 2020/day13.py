import numpy as np
import math

def parseInput():
    with open('input.txt', 'r') as f:
        elems = f.readlines()
    time = int(elems[0].strip())
    buses = []
    for option in elems[1].strip().split(','):
        if option == 'x':
            pass
        else:
            buses.append(int(option))
    return [time, buses]


def partOne():
    time, buses = parseInput()
    print(time, len(buses), buses)
    scores = []
    for bus in buses:
        timeSinceLeft = (time % bus)
        scores.append([bus - timeSinceLeft, bus])
    busesSorted = sorted(scores, key=lambda x: x[0])
    print(busesSorted)
    print(busesSorted[0][0] * busesSorted[0][1])

# partOne()
'''
t mod 29 = 0
t mod 41 = 22
t mod 577 = 548
t mod 13 = 10
t mod 17 = 8
t mod 19 = 9
t mod 23 = 17
t mod 601 = 541
t mod 37 = 14
...
[[29, 0], [41, 19], [577, 29], [13, 42], [17, 43], [19, 48], [23, 52], [601, 60], [37, 97]]

t mod 29 = 0
t + 19 mod 41 = 0

29x + 0 = 41y + 19 = 577z + 29 = 13a + 42 = 17b + 43
29x - 41y = 19
'''

def parseInput2():
    with open('input.txt', 'r') as f:
        elems = f.readlines()
    buses = []
    offset = 0
    for bus in elems[1].strip().split(','): 
        if bus != 'x':
            buses.append([int(bus), offset])
        offset += 1
    return buses 

def rotations(mod1, offset1, mod2, offset2):
    found = False
    val = offset1
    count = 0
    while not found:
        count += 1
        val += mod1
        if (val % mod2) == offset2:
            found = True
            print(count, val)
            return val

def myLCM(a, b):
    return a*b // math.gcd(a, b)

def partTwo():
    # buses = sorted(parseInput2(), reverse=True, key=lambda x: x[0])
    buses = parseInput2()
    numBuses = len(buses)
    print(buses)
    multiples = []
    m1, o1 = buses[0]
    for bus in buses[1:]:
        m2, o2 = bus
        firstIntersect = rotations(m2, (0-o2) % m2, m1, (0-o1) % m1)
        pairPeriod = myLCM(m1, m2)
        multiples.append([firstIntersect, pairPeriod])
    print(multiples)
    currPos = multiples[0][0]
    currPer = multiples[0][1]
    for mult in multiples[1:]:
        firstCross, period = mult 
        found = False
        while not found:
            if currPos == firstCross:
                print('intersect!', currPos)
                found = True
            elif currPos > firstCross:
                firstCross += period 
            else:
                currPos += currPer 
        currPer = myLCM(currPer, period)
        print('period', currPer)
    print(currPos, currPer)

    # period = 1
    # for m in multiples:
    #     period = myLCM(period, m)
    # print(period)

# 952626856
partTwo()

'''
[[145, 1189], [16704, 16733], [348, 377], [348, 493], [522, 551], [638, 667], [4147, 17429], [754, 1073]]
intersect! 33437
intersect! 8266073
intersect! 88534274
intersect! 2211182256
intersect! 28137811179
intersect! 24013150301501
'''