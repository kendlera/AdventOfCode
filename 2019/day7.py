from itertools import permutations

def parseInput():
	f = open("input.txt", 'r')
	insts = f.read().strip()
	arr = insts.split(",")
	intArr = []
	for elem in arr:
		intArr.append(int(elem))
	return intArr 

def parseOpcode(code):
	if code < 10:
		return (0, 0, code)
	elif code < 199:
		return (1, 0, code-100)
	else:
		strRepr = str(code)
		mode1 = strRepr[1]
		code = code - (int("1"+mode1) * 100)
		return (int(mode1), 1, code)

def intCodesComputer(inputs, currPos):
	inputIdx = 0
	outputs = []
	codes = parseInput()
	# currPos = 0
	while (codes[currPos] != 99):
		opcode = codes[currPos]
		mode1, mode2, opcode = parseOpcode(opcode)
		if opcode == 1:
			# addition
			val1 = codes[currPos+1] if mode1 == 1 else codes[codes[currPos+1]]
			val2 = codes[currPos+2] if mode2 == 1 else codes[codes[currPos+2]]
			codes[codes[currPos+3]] = (val1 + val2)
			currPos += 4
		elif opcode == 2:
			# multiplication
			val1 = codes[currPos+1] if mode1 == 1 else codes[codes[currPos+1]]
			val2 = codes[currPos+2] if mode2 == 1 else codes[codes[currPos+2]]
			codes[codes[currPos+3]] = (val1 * val2)
			currPos += 4
		elif opcode == 3:
			# place input
			# if we're out of inputs, we just return our outputs and wait
			if (len(inputs) == inputIdx):
				return (currPos, outputs)
			codes[codes[currPos+1]] = inputs[inputIdx]
			inputIdx += 1
			currPos += 2
		elif opcode == 4:
			# print output
			val1 = codes[currPos+1] if mode1 == 1 else codes[codes[currPos+1]]
			outputs.append(val1)
			# print("Output", val1)
			currPos += 2
		elif opcode == 5:
			# jump if true
			val1 = codes[currPos+1] if mode1 == 1 else codes[codes[currPos+1]]
			val2 = codes[currPos+2] if mode2 == 1 else codes[codes[currPos+2]]
			if val1 != 0:
				currPos = val2 
			else:
				currPos += 3 
		elif opcode == 6:
			# jump if false
			val1 = codes[currPos+1] if mode1 == 1 else codes[codes[currPos+1]]
			val2 = codes[currPos+2] if mode2 == 1 else codes[codes[currPos+2]]
			if val1 == 0:
				currPos = val2 
			else:
				currPos += 3
		elif opcode == 7:
			# less than
			val1 = codes[currPos+1] if mode1 == 1 else codes[codes[currPos+1]]
			val2 = codes[currPos+2] if mode2 == 1 else codes[codes[currPos+2]]
			valToStore = 1 if val1 < val2 else 0
			codes[codes[currPos+3]] = valToStore
			currPos += 4
		elif opcode == 8:
			val1 = codes[currPos+1] if mode1 == 1 else codes[codes[currPos+1]]
			val2 = codes[currPos+2] if mode2 == 1 else codes[codes[currPos+2]]
			valToStore = 1 if val1 == val2 else 0
			codes[codes[currPos+3]] = valToStore
			currPos += 4
		else:
			print("Something went wrong")
			return []
	return (-1, outputs) # -1 indicates that this amplifier is done executing


def processAmplifiers():
	phaseCombos = permutations([5, 6, 7, 8, 9])
	scores = []
	for combo in phaseCombos:
		seeds = [0]
		done = False
		firstPass = True
		ampPositions = [0, 0, 0, 0, 0]
		while not done:
			for ampNum in range(0, 5):
				inputs = [combo[ampNum]] if firstPass else []
				ampPos, outputs = intCodesComputer(inputs + seeds, ampPositions[ampNum])
				if len(outputs) == 0:
					print("No Output!")
					return
				ampPositions[ampNum] = ampPos
				seeds = outputs
				if firstPass and ampNum == 4:
					firstPass = False
				if ampPos == -1 and ampNum == 4:
					if (len(outputs) != 1):
						print("Not sure how to handle")
					done = True
		scores.append([seeds[0], combo])
	print(sorted(scores, key = lambda x: x[0], reverse=True))

# processAmplifiers()