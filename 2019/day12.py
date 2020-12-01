'''
<x=17, y=-9, z=4>
<x=2, y=2, z=-13>
<x=-1, y=5, z=-1>
<x=4, y=7, z=-7>
'''

def planetsOrbit():
	startPos = []
	startPos.append([17, -9, 4])
	startPos.append([2, 2, -13])
	startPos.append([-1, 5, -1])
	startPos.append([4, 7, -7])

	positions = []
	positions.append([17, -9, 4])
	positions.append([2, 2, -13])
	positions.append([-1, 5, -1])
	positions.append([4, 7, -7])

	velocities = []
	velocities.append([0, 0, 0])
	velocities.append([0, 0, 0])
	velocities.append([0, 0, 0])
	velocities.append([0, 0, 0])

	numSteps = 0
	stepping = True
	while stepping:
		# adjust velocities
		for x in range(0, 4):
			for y in range(x+1, 4):
				for axis in range(0, 3):
					if positions[x][axis] == positions[y][axis]:
						continue
					elif positions[x][axis] < positions[y][axis]:
						velocities[x][axis] = (velocities[x][axis] + 1)
						velocities[y][axis] = (velocities[y][axis] - 1)
					else:
						velocities[x][axis] = (velocities[x][axis] - 1)
						velocities[y][axis] = (velocities[y][axis] + 1)

		# allZeros = True
		for planet in range(0, 4):
			hasMatch = True
			for axis in range(0, 3):
				positions[planet][axis] = (positions[planet][axis] + velocities[planet][axis]) 
				if positions[planet][axis] != startPos[planet][axis]:
					hasMatch = False
			if hasMatch:
				print("Steps for Planet", planet, ":", numSteps)

		numSteps += 1

	# energy is the sum of the absolute values multiplied together
	total = 0
	for planet in range(0, 4):
		sumVel = 0
		sumPos = 0
		for axis in range(0, 3):
			sumVel += abs(velocities[planet][axis])
			sumPos += abs(positions[planet][axis])
		total += (sumVel * sumPos)

	print(total)



planetsOrbit()