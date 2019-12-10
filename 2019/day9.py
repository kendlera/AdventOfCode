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
		return (0, 0, 0, code)
	elif code < 999:
		strRepr = str(code)
		mode1 = int(strRepr[0])
		return (mode1, 0, 0, code-(mode1 * 100))
	elif code < 9999:
		strRepr = str(code)
		mode1 = strRepr[1]
		mode2 = strRepr[0]
		code = code - (int(mode2+mode1) * 100)
		return (int(mode1), int(mode2), 0, code)
	else:
		strRepr = str(code)
		mode1 = strRepr[2]
		mode2 = strRepr[1]
		mode3 = strRepr[0]
		code = code - (int(mode3+mode2+mode1) * 100)
		return (int(mode1), int(mode2), int(mode3), code)

def intCodesComputer(inputs, relativeBase):
	inputIdx = 0
	outputs = []
	codes = parseInput() + [0] * 1000 # make this bigger if we get OOM
	currPos = 0
	while (codes[currPos] != 99):
		opcode = codes[currPos]
		mode1, mode2, mode3, opcode = parseOpcode(opcode)
		# print(mode1, mode2, mode3, opcode)
		if opcode == 1:
			# addition
			param1 = codes[currPos+1] + relativeBase if mode1 == 2 else codes[currPos+1]
			param2 = codes[currPos+2] + relativeBase if mode2 == 2 else codes[currPos+2]
			param3 = codes[currPos+3] + relativeBase if mode3 == 2 else codes[currPos+3]
			val1 = codes[currPos+1] if mode1 == 1 else codes[param1]
			val2 = codes[currPos+2] if mode2 == 1 else codes[param2]
			codes[param3] = (val1 + val2)
			currPos += 4
		elif opcode == 2:
			# multiplication
			param1 = codes[currPos+1] + relativeBase if mode1 == 2 else codes[currPos+1]
			param2 = codes[currPos+2] + relativeBase if mode2 == 2 else codes[currPos+2]
			param3 = codes[currPos+3] + relativeBase if mode3 == 2 else codes[currPos+3]
			val1 = codes[currPos+1] if mode1 == 1 else codes[param1]
			val2 = codes[currPos+2] if mode2 == 1 else codes[param2]
			codes[param3] = (val1 * val2)
			currPos += 4
		elif opcode == 3:
			# place input
			param1 = codes[currPos+1] + relativeBase if mode1 == 2 else codes[currPos+1]
			codes[param1] = inputs[inputIdx]
			inputIdx += 1
			currPos += 2
		elif opcode == 4:
			# print output
			param1 = codes[currPos+1] + relativeBase if mode1 == 2 else codes[currPos+1]
			val1 = codes[currPos+1] if mode1 == 1 else codes[param1]
			outputs.append(val1)
			print("Output", val1)
			currPos += 2
		elif opcode == 5:
			# jump if true
			param1 = codes[currPos+1] + relativeBase if mode1 == 2 else codes[currPos+1]
			param2 = codes[currPos+2] + relativeBase if mode2 == 2 else codes[currPos+2]
			val1 = codes[currPos+1] if mode1 == 1 else codes[param1]
			val2 = codes[currPos+2] if mode2 == 1 else codes[param2]
			if val1 != 0:
				currPos = val2 
			else:
				currPos += 3 
		elif opcode == 6:
			# jump if false
			param1 = codes[currPos+1] + relativeBase if mode1 == 2 else codes[currPos+1]
			param2 = codes[currPos+2] + relativeBase if mode2 == 2 else codes[currPos+2]
			val1 = codes[currPos+1] if mode1 == 1 else codes[param1]
			val2 = codes[currPos+2] if mode2 == 1 else codes[param2]
			if val1 == 0:
				currPos = val2 
			else:
				currPos += 3
		elif opcode == 7:
			# less than
			param1 = codes[currPos+1] + relativeBase if mode1 == 2 else codes[currPos+1]
			param2 = codes[currPos+2] + relativeBase if mode2 == 2 else codes[currPos+2]
			param3 = codes[currPos+3] + relativeBase if mode3 == 2 else codes[currPos+3]
			val1 = codes[currPos+1] if mode1 == 1 else codes[param1]
			val2 = codes[currPos+2] if mode2 == 1 else codes[param2]
			valToStore = 1 if val1 < val2 else 0
			codes[param3] = valToStore
			currPos += 4
		elif opcode == 8:
			param1 = codes[currPos+1] + relativeBase if mode1 == 2 else codes[currPos+1]
			param2 = codes[currPos+2] + relativeBase if mode2 == 2 else codes[currPos+2]
			param3 = codes[currPos+3] + relativeBase if mode3 == 2 else codes[currPos+3]
			val1 = codes[currPos+1] if mode1 == 1 else codes[param1]
			val2 = codes[currPos+2] if mode2 == 1 else codes[param2]
			valToStore = 1 if val1 == val2 else 0
			codes[param3] = valToStore
			currPos += 4
		elif opcode == 9:
			# adjust relative base
			param1 = codes[currPos+1] + relativeBase if mode1 == 2 else codes[currPos+1]
			val1 = codes[currPos+1] if mode1 == 1 else codes[param1]
			relativeBase += val1
			currPos += 2
		else:
			print("Something went wrong")
			return []


def processAmplifiers():
	relativeBase = 0
	intCodesComputer([2], 0)

# processAmplifiers()