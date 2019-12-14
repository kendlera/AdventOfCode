import copy

def parseInput():
	f = open("input.txt", 'r')
	myInput = f.readlines()
	myMap = []
	for line in myInput:
		myMap.append(line.strip())
	return myMap

def getGCD(a,b): 
	# return the greatest common denominator
    if(b==0): 
        return a 
    else: 
        return getGCD(b,a%b) 

def getSlope(start, end):
	sX, sY = start 
	eX, eY = end
	xDiff = eX - sX
	yDiff = eY - sY
	if xDiff == 0 or yDiff == 0:
		# no simplification possible
		slope = [0, yDiff/(abs(yDiff))] if xDiff == 0 else [xDiff/abs(xDiff), 0]
		return slope
	gcd = getGCD(abs(xDiff), abs(yDiff))
	slope = [(xDiff/gcd), (yDiff/gcd)]
	return slope

def clearHidden(pos, slope, elem):
	# clears the current asteroid and all asteroids behind it
	posX, posY = pos 
	distX, distY = slope 
	hiding = True
	maxDist = len(elem)
	distMult = 0
	while (hiding):
		currX = int(posX + (distX * distMult))
		currY = int(posY + (distY * distMult))
		# print("Clearing", [currX, currY])
		if (currX >= maxDist) or (currY >= maxDist) or (currX < 0) or (currY < 0):
			# out of bounds
			hiding = False
			return elem
		try:
			row = elem[currY][:currX] + "-" + elem[currY][(currX+1):]
			if len(row) > len(elem[currY]):
				print("Something Wrong - (", currX, ",", currY, ")")
			elem[currY] = row
		except e:
			raise e
			hiding = False
		distMult += 1
	return elem

def countAsteroids(pos, elem):
	# count how many asteroids are visible from pos
	# change all invisible asteroids to "." and then 
	# count remaining "#"
	posX, posY = pos 
	maxDist = len(elem)
	distFromPos = 1
	done = False
	count = 0
	while not done:
		for x in range(0, distFromPos+1):
			y = distFromPos - x
			currX = (posX + x)
			currY = (posY + y)
			if (currX < maxDist and currY < maxDist and currX >= 0 and currY >= 0):
				if elem[currY][currX] == "#":
					# print("Found Asteroid at (", currX, ", ", currY, ")")
					count += 1
					slope = getSlope(pos, [currX, currY])
					elem = clearHidden([currX, currY], slope, elem)
			currX = (posX - x)
			currY = (posY + y)
			if (currX < maxDist and currY < maxDist and currX >= 0 and currY >= 0):
				if elem[currY][currX] == "#":
					# print("Found Asteroid at (", currX, ", ", currY, ")")
					count += 1
					slope = getSlope(pos, [currX, currY])
					elem = clearHidden([currX, currY], slope, elem)
			currX = (posX + x)
			currY = (posY - y)
			if (currX < maxDist and currY < maxDist and currX >= 0 and currY >= 0):
				if elem[currY][currX] == "#":
					# print("Found Asteroid at (", currX, ", ", currY, ")")
					count += 1
					slope = getSlope(pos, [currX, currY])
					elem = clearHidden([currX, currY], slope, elem)
			currX = (posX - x)
			currY = (posY - y)
			if (currX < maxDist and currY < maxDist and currX >= 0 and currY >= 0):
				if elem[currY][currX] == "#":
					# print("Found Asteroid at (", currX, ", ", currY, ")")
					count += 1
					slope = getSlope(pos, [currX, currY])
					elem = clearHidden([currX, currY], slope, elem)
		distFromPos += 1
		if distFromPos > (maxDist *2):
			# we're at the edge of the map
			done = True
	for line in elem:
		print(line)
	return count


def findBestPlace():
	myMap = parseInput()
	counts = []
	numEval = 0
	for x in range(0, len(myMap[0])):
		for y in range(0, len(myMap)):
			if myMap[y][x] == "#":
				# print("Evaluating (", x, ",", y, ")" )
				mapCopy = copy.deepcopy(myMap)
				numView = countAsteroids([x, y], mapCopy)
				counts.append([numView, [x, y]])
	print(sorted(counts, key=lambda x: x[0], reverse=True))

# findBestPlace()


# PART TWO

QUADRANTS = {}
# build up a sorted list of all the slopes by quadrant
def initQuadrants():
	center = [20, 19] # solution from part 1
	maxDist = 26
	slopesScores = []
	slopes = []
	for x in range(center[0]+1, maxDist):
		for y in range(0, center[1]):
			# calculate slopes for every point in quadrant 1
			slope = getSlope(center, [x, y])
			if slope not in slopes:
				slopes.append(slope)
				slopesScores.append(slope[0]/slope[1])
	# sort ascending
	join = [[slopes[x], slopesScores[x]] for x in range(len(slopes))]
	final = sorted(join, key=lambda x: x[1], reverse=True)
	QUADRANTS[1] = final
	# print(final)
	slopesScores = []
	slopes = []
	for x in range(center[0]+1, maxDist):
		for y in range(center[1]+1, maxDist):
			# calculate slopes for every point in quadrant 1
			slope = getSlope(center, [x, y])
			if slope not in slopes:
				slopes.append(slope)
				slopesScores.append(slope[0]/slope[1])
	# sort ascending
	join = [[slopes[x], slopesScores[x]] for x in range(len(slopes))]
	final = sorted(join, key=lambda x: x[1], reverse=True)
	QUADRANTS[2] = final
	# print(final)

	slopesScores = []
	slopes = []
	for x in range(0, center[0]):
		for y in range(center[1]+1, maxDist):
			# calculate slopes for every point in quadrant 1
			slope = getSlope(center, [x, y])
			if slope not in slopes:
				slopes.append(slope)
				slopesScores.append(slope[0]/slope[1])
	# sort ascending
	join = [[slopes[x], slopesScores[x]] for x in range(len(slopes))]
	final = sorted(join, key=lambda x: x[1], reverse=True)
	QUADRANTS[3] = final
	# print(final)

	slopesScores = []
	slopes = []
	for x in range(0, center[0]):
		for y in range(0, center[1]):
			# calculate slopes for every point in quadrant 1
			slope = getSlope(center, [x, y])
			if slope not in slopes:
				slopes.append(slope)
				slopesScores.append(slope[0]/slope[1])
	# sort ascending
	join = [[slopes[x], slopesScores[x]] for x in range(len(slopes))]
	final = sorted(join, key=lambda x: x[1], reverse=True)
	QUADRANTS[4] = final
	# print(final)

def getNextPoint(prevCoord):
	quadrantNum, idx = prevCoord
	if type(idx) == list:
		return [quadrantNum, 0]
	elif (len(QUADRANTS[quadrantNum]) - 1) == idx:
		# we're at the end of that quadrant
		if quadrantNum == 1:
			return (2, [1, 0])
		elif quadrantNum == 2:
			return (3, [0, 1])
		elif quadrantNum == 3:
			return (4, [-1, 0])
		else:
			return(1, [0, -1])
	else:
		return [quadrantNum, idx+1]

def destroyAsteroid(pos, slope, myMap):
	firing = True
	fireDist = 1
	maxDist = len(myMap)
	posX, posY = pos 
	slopeX, slopeY = slope 
	while firing:
		currX = int(posX + (slopeX * fireDist))
		currY = int(posY + (slopeY * fireDist))
		if (currX < maxDist and currY < maxDist and currX >= 0 and currY >= 0):
			if myMap[currY][currX] == "#":
				# we hit an asteroid!
				row = myMap[currY][:currX] + "-" + myMap[currY][(currX+1):]
				myMap[currY] = row 
				return ([currX, currY], myMap) 
		else:
			# we went off the map without hitting anything
			return (None, myMap)
		fireDist += 1

def vaporizeAsteroids():
	pos = [20, 19] # solution from part 1
	lastPoint = [4, len(QUADRANTS[4]) - 1]
	numHit = 0
	myMap = parseInput()
	myMap[19] = myMap[19][:20] + "X" + myMap[19][21:]
	done = False
	while not done:
		# go around the edge of the box and vaporize asteroids
		nextPoint = getNextPoint(lastPoint)
		if type(nextPoint[1]) == int:
			quadrantNum, idx = nextPoint
			slope = QUADRANTS[quadrantNum][idx][0]
		else:
			slope = nextPoint[1]
		hitPos, myMap = destroyAsteroid(pos, slope, myMap)
		lastPoint = nextPoint
		if hitPos is not None:
			# we hit an asteroid!
			print("Hit", numHit+1, "asteroids")
			print(slope, ":", hitPos)
			for line in myMap:
				print(line)
			print("---------------------------------------")
			numHit += 1
			if numHit == 200:
				# we hit our 200th asteroid!
				print(hitPos)
				return

initQuadrants()
vaporizeAsteroids()