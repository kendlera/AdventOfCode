

def readInput():
	f = open("input.txt", "r")
	instructions = []
	for line in f:
		center, orbiter = line.strip().split(")")
		instructions.append([center, orbiter])
	return instructions

# part 1
def processInst():
	insts = readInput()
	orbits = {} # map direct orbits
	for inst in insts:
		orbits[inst[1]] = inst[0]
	# now count direct and indirect orbits
	numOrbits = 0
	for outerMost in orbits:
		currObj = outerMost
		done = False
		while not done:
			if currObj not in orbits:
				done = False
				break
			numOrbits += 1
			currObj = orbits[currObj]
	print(numOrbits)

# processInst()

def getDists(orbits, obj):
	currObj = orbits[obj]
	dists = {}
	steps = 0
	done = False
	while not done:
		dists[currObj] = steps
		steps += 1
		currObj = orbits[currObj]
		if currObj not in orbits:
			done = True
			break
	return dists

def calculateOrbits():
	insts = readInput()
	orbits = {} # map direct orbits
	for inst in insts:
		orbits[inst[1]] = inst[0]
	# calculate steps from YOU to all downstream orbit options
	youSteps = getDists(orbits, "YOU")
	sanSteps = getDists(orbits, "SAN")
	possiblePaths = []
	for step in youSteps:
		if step in sanSteps:
			# it's a shared node!
			possiblePaths.append(youSteps[step] + sanSteps[step])

	print(sorted(possiblePaths))

# calculateOrbits()