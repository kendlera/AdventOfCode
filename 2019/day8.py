
def parseInput():
	f = open("input.txt", 'r')
	nums = f.read().strip()
	return nums

def processData():
	info = parseInput()
	numPerLayer = 25 * 6
	idx = 0
	counts = []
	layers = int(len(info) / numPerLayer)
	# print("Num Layers:", layers)
	for layer in range(0, layers):
		zeros, ones, twos = (0, 0, 0)
		for elem in range(0, numPerLayer):
			if info[idx] == "0": 
				zeros += 1
			elif info[idx] == "1":
				ones += 1
			elif info[idx] == "2":
				twos += 1
			idx += 1
		counts.append([zeros, ones * twos])
	print(sorted(counts, key= lambda x: x[0]))

# processData()

def getMessage():
	info = parseInput()
	layers = int(len(info) / (25*6))
	idx = 0
	allMsgs = []
	for r in range(0, 6):
		allMsgs.append(["2"] * 25)
	for layer in range(0, layers):
		for row in range(0, len(allMsgs)):
			for col in range(0, len(allMsgs[0])):
				if allMsgs[row][col] == "2":
					# still transparent
					allMsgs[row][col] = info[idx]
				idx += 1

	for row in allMsgs:
		print("".join(["*" if r == "1" else " " for r in row]))

# getMessage()
