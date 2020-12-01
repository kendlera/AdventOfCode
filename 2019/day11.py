from incodeComputer import IntcodeComputer

def parseInput():
	f = open("input.txt", 'r')
	insts = f.read().strip()
	arr = insts.split(",")
	intArr = []
	for elem in arr:
		intArr.append(int(elem))
	return intArr 

def printGrid(grid, pos):
	for row in grid:
		rowRepr = ["," if x == 1 else "." for x in row]
		print("".join(rowRepr))
	print("\n\n")

def rotateRobot(currDir, inst):
	if currDir == "UP":
		if inst == 0:
			return "LEFT"
		return "RIGHT"
	elif currDir == "LEFT":
		if inst == 0:
			return "DOWN"
		return "UP"
	elif currDir == "RIGHT":
		if inst == 0:
			return "UP"
		return "DOWN"
	else:
		# DOWN
		if inst == 0:
			return "RIGHT"
		return "LEFT"

def runRobot():
	# make a 100 x 100 grid
	grid = []
	for row in range(0, 100):
		grid.append([0] * 100)

	# make a robot
	robot = IntcodeComputer(parseInput())
	robotPos = [50,50]
	robotDir = "UP"

	visited = [robotPos]

	# part 2 - start with a white panel
	x, y = robotPos 
	grid[y][x] = 1

	done = False
	paintInst = True
	while not done:
		x, y = robotPos
		# need to move sequentially
		output, done = robot.runComputer([])
		while output is None and not done:
			x, y = robotPos
			output, done = robot.runComputer([grid[y][x]])

		if done:
			break

		if paintInst:
			grid[y][x] = output
			paintInst = False 
			if robotPos not in visited:
				visited.append(robotPos)
		else:
			# move the robot
			robotDir = rotateRobot(robotDir, output)
			if robotDir == "UP":
				robotPos = [robotPos[0], robotPos[1]-1] 
			elif robotDir == "LEFT":
				robotPos = [robotPos[0]-1, robotPos[1]] 
			elif robotDir == "DOWN":
				robotPos = [robotPos[0], robotPos[1]+1]
			else: # RIGHT
				robotPos = [robotPos[0]+1, robotPos[1]]  
			paintInst = True
			# printGrid(grid, robotPos)

	printGrid(grid, robotPos)
	print("Visited Squares:", len(visited))

# runRobot()