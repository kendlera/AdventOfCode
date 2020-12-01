from incodeComputer import IntcodeComputer
import random

def parseInput():
	f = open("input.txt", 'r')
	insts = f.read().strip()
	arr = insts.split(",")
	intArr = []
	for elem in arr:
		intArr.append(int(elem))
	return intArr 

def getOutputs():
	myGame = IntcodeComputer(parseInput())
	outputs = []
	done = False
	while not done:
		output, done = myGame.runComputer([random.choice([-1, 0, 1])]) 
		if done:
			break
		outputs.append(output)
	return outputs 

def countBlocks(gameState):
	blocks = 0
	# count blocks
	for i in range(2, len(gameState), 3):
		if gameState[i] == 2:
			blocks += 1
	return blocks

def drawGame():
	gameInstructions = getOutputs()
	print(gameInstructions)
	blockCounts = countBlocks(gameInstructions)
	print("Blocks", blockCounts)
	for i in range(0, len(gameInstructions), 3):
		if gameInstructions[i] == -1:
			if gameInstructions[i+1] == 0:
				print("Player Score:", gameInstructions[i+2])

drawGame()
