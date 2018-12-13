
function parseInput(filename)
	fd = open(filename, "r")
	input = read(fd, String)
	inputs = split(input, "\n")
	transforms = Dict()
	for i in inputs
		pattern, result = split(i, " => ")
		transforms[pattern] = result
	end
	return transforms
end

function projectGenerations(transforms, numGenerations)
	currentState = "..#..###...#####.#.#...####.#..####..###.##.#.#.##.#....#....#.####...#....###.###..##.#....#######" 
	idx0 = 1
	for g=1:numGenerations
		newGen = ".."
		# add on more pots if necessary
		if currentState[1:4] != "...."
			currentState = "...." * currentState
			idx0 += 4
		end
		if currentState[end-3:end] != "...."
			currentState = currentState * "...."
		end
		for i=3:length(currentState)-2
			newPot = get(transforms, currentState[i-2:i+2], ".")
			newGen = newGen * newPot
		end
		currentState = newGen
	end
	startIdx = 1-idx0
	total = 0
	for x=1:length(currentState)
		if string(currentState[x]) == "#"
			total += startIdx 
		end
		startIdx += 1
	end
	return total
end

filename = "/Users/akendler/Documents/personal/AdventofCode/input.txt"
println(projectGenerations(parseInput(filename), 20))