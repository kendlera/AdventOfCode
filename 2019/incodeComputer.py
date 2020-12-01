class IntcodeComputer() :

	def __init__(self, instructions):
		# do nothing
		self.currPos = 0
		self.instructions = instructions + [0] * 1000 # make this bigger if we get OOM
		self.relativeBase = 0
		self.inputs = []
		self.outputs = []

	def runComputer(self, inputs):
		self.inputs = inputs
		# print("Running Incode From", self.currPos, "with", self.inputs)
		return self.intCodesComputer()

	def parseOpcode(self, code):
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

	def intCodesComputer(self):
		inputIdx = 0
		while (self.instructions[self.currPos] != 99):
			opcode = self.instructions[self.currPos]
			mode1, mode2, mode3, opcode = self.parseOpcode(opcode)
			# print(mode1, mode2, mode3, opcode)
			if opcode == 1:
				# addition
				param1 = self.instructions[self.currPos+1] + self.relativeBase if mode1 == 2 else self.instructions[self.currPos+1]
				param2 = self.instructions[self.currPos+2] + self.relativeBase if mode2 == 2 else self.instructions[self.currPos+2]
				param3 = self.instructions[self.currPos+3] + self.relativeBase if mode3 == 2 else self.instructions[self.currPos+3]
				val1 = self.instructions[self.currPos+1] if mode1 == 1 else self.instructions[param1]
				val2 = self.instructions[self.currPos+2] if mode2 == 1 else self.instructions[param2]
				self.instructions[param3] = (val1 + val2)
				self.currPos += 4
			elif opcode == 2:
				# multiplication
				param1 = self.instructions[self.currPos+1] + self.relativeBase if mode1 == 2 else self.instructions[self.currPos+1]
				param2 = self.instructions[self.currPos+2] + self.relativeBase if mode2 == 2 else self.instructions[self.currPos+2]
				param3 = self.instructions[self.currPos+3] + self.relativeBase if mode3 == 2 else self.instructions[self.currPos+3]
				val1 = self.instructions[self.currPos+1] if mode1 == 1 else self.instructions[param1]
				val2 = self.instructions[self.currPos+2] if mode2 == 1 else self.instructions[param2]
				self.instructions[param3] = (val1 * val2)
				self.currPos += 4
			elif opcode == 3:
				# place input
				if len(self.inputs) <= inputIdx:
					self.inputs = []
					print("No More Inputs, Returning")
					return None, False
				print("Using", self.inputs[inputIdx], "for input")
				param1 = self.instructions[self.currPos+1] + self.relativeBase if mode1 == 2 else self.instructions[self.currPos+1]
				self.instructions[param1] = self.inputs[inputIdx]
				inputIdx += 1
				self.currPos += 2
			elif opcode == 4:
				# print output
				param1 = self.instructions[self.currPos+1] + self.relativeBase if mode1 == 2 else self.instructions[self.currPos+1]
				val1 = self.instructions[self.currPos+1] if mode1 == 1 else self.instructions[param1]
				# self.outputs.append(val1)
				# print("Output", val1)
				self.currPos += 2
				self.inputs = []
				return val1, False
			elif opcode == 5:
				# jump if true
				param1 = self.instructions[self.currPos+1] + self.relativeBase if mode1 == 2 else self.instructions[self.currPos+1]
				param2 = self.instructions[self.currPos+2] + self.relativeBase if mode2 == 2 else self.instructions[self.currPos+2]
				val1 = self.instructions[self.currPos+1] if mode1 == 1 else self.instructions[param1]
				val2 = self.instructions[self.currPos+2] if mode2 == 1 else self.instructions[param2]
				if val1 != 0:
					self.currPos = val2 
				else:
					self.currPos += 3 
			elif opcode == 6:
				# jump if false
				param1 = self.instructions[self.currPos+1] + self.relativeBase if mode1 == 2 else self.instructions[self.currPos+1]
				param2 = self.instructions[self.currPos+2] + self.relativeBase if mode2 == 2 else self.instructions[self.currPos+2]
				val1 = self.instructions[self.currPos+1] if mode1 == 1 else self.instructions[param1]
				val2 = self.instructions[self.currPos+2] if mode2 == 1 else self.instructions[param2]
				if val1 == 0:
					self.currPos = val2 
				else:
					self.currPos += 3
			elif opcode == 7:
				# less than
				param1 = self.instructions[self.currPos+1] + self.relativeBase if mode1 == 2 else self.instructions[self.currPos+1]
				param2 = self.instructions[self.currPos+2] + self.relativeBase if mode2 == 2 else self.instructions[self.currPos+2]
				param3 = self.instructions[self.currPos+3] + self.relativeBase if mode3 == 2 else self.instructions[self.currPos+3]
				val1 = self.instructions[self.currPos+1] if mode1 == 1 else self.instructions[param1]
				val2 = self.instructions[self.currPos+2] if mode2 == 1 else self.instructions[param2]
				valToStore = 1 if val1 < val2 else 0
				self.instructions[param3] = valToStore
				self.currPos += 4
			elif opcode == 8:
				param1 = self.instructions[self.currPos+1] + self.relativeBase if mode1 == 2 else self.instructions[self.currPos+1]
				param2 = self.instructions[self.currPos+2] + self.relativeBase if mode2 == 2 else self.instructions[self.currPos+2]
				param3 = self.instructions[self.currPos+3] + self.relativeBase if mode3 == 2 else self.instructions[self.currPos+3]
				val1 = self.instructions[self.currPos+1] if mode1 == 1 else self.instructions[param1]
				val2 = self.instructions[self.currPos+2] if mode2 == 1 else self.instructions[param2]
				valToStore = 1 if val1 == val2 else 0
				self.instructions[param3] = valToStore
				self.currPos += 4
			elif opcode == 9:
				# adjust relative base
				param1 = self.instructions[self.currPos+1] + self.relativeBase if mode1 == 2 else self.instructions[self.currPos+1]
				val1 = self.instructions[self.currPos+1] if mode1 == 1 else self.instructions[param1]
				self.relativeBase += val1
				self.currPos += 2
			else:
				print("Something went wrong")
				return [], True
		print("Reached End Of Execution")
		myOutputs = self.outputs
		self.outputs = []
		self.inputs = []
		return None, True
