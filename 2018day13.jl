

mutable struct cart
	coords::Array
	direction::String
	lastTurn::String
end

function parseInput(filename)
	fd = open(filename, "r")
	input = read(fd, String)
	inputs = split(input, "\n")
	carts = [] # contains arrays of [[x, y], direction, last_turn]
	cart_options = ["<", ">", "^", "v"]
	for lineIdx=1:length(inputs)
		for c in cart_options 
			replacing = true
			while replacing
				result = findfirst(c, inputs[lineIdx])
				if result == nothing
					replacing = false
				else
					xcoord = result[1]
					cart_info = cart([lineIdx, xcoord], c, "r")
					push!(carts, cart_info)
					# replace map
					# above, below, left, right
					pathPresent = [false, false, false, false]
					pathPresent[1] = lineIdx > 1 && occursin(string(inputs[lineIdx-1][xcoord]), "|+/\\")
					pathPresent[2] = lineIdx < length(inputs) && occursin(string(inputs[lineIdx+1][xcoord]), "|+/\\")
					pathPresent[3] = xcoord > 1 && occursin(string(inputs[lineIdx][xcoord-1]), "-+/\\")
					pathPresent[4] = xcoord < length(inputs[lineIdx]) && occursin(string(inputs[lineIdx][xcoord+1]), "-+/\\")
					if !in(false, pathPresent)
						# we're at an intersection 
						token = "+"
					elseif pathPresent[1] && pathPresent[2]
						token = "|"
					elseif pathPresent[3] && pathPresent[4]
						token = "-"
					elseif (pathPresent[1] && pathPresent[4]) || (pathPresent[2] && pathPresent[3])
						token = "\\" 
					elseif (pathPresent[1] && pathPresent[3]) || (pathPresent[2] && pathPresent[4])
						token = "/"
					else
						println(pathPresent)
						println(inputs[lineIdx-1])
						println(inputs[lineIdx])
						println(inputs[lineIdx+1])
						println("Error, no valid markers! [", lineIdx, ", ", xcoord, "]")
					end
					if xcoord == 1
						inputs[lineIdx] = token * inputs[lineIdx][2:end]
					elseif xcoord == length(inputs[lineIdx])
						inputs[lineIdx] = inputs[lineIdx][1:end-1] * token
					else
						inputs[lineIdx] = inputs[lineIdx][1:xcoord-1] * token * inputs[lineIdx][xcoord+1:end]
					end
				end
			end
		end
	end
	return inputs, carts
end

function pushCarts(rails, carts)
	time = 0
	numCarts = length(carts)
	keepGoing = true
	directions = Dict{String, Array}("^"=>[-1, 0], ">"=>[0, 1], "v"=>[1, 0], "<"=>[0, -1])
	turnLeft = Dict{String, String}("^"=>"<", "<"=>"v", "v"=>">", ">"=>"^")
	turnRight = Dict{String, String}("^"=>">", "<"=>"^", "v"=>"<", ">"=>"v")
	while true
		sort!(carts, by = x->x.coords[1])
		if numCarts == 1
			keepGoing = false
		end
		for c=1:length(carts)
			if carts[c].coords == [0, 0]
				continue
			end
			# move the cart
			token = string(rails[carts[c].coords[1]][carts[c].coords[2]])
			if token == "+"
				# turn in the intersection
				if carts[c].lastTurn == "r"
					carts[c].lastTurn = "l"
					carts[c].direction = turnLeft[carts[c].direction]
				elseif carts[c].lastTurn == "l"
					carts[c].lastTurn = "s"
				else 
					carts[c].lastTurn = "r"
					carts[c].direction = turnRight[carts[c].direction]
				end
			elseif token == "/"
				if occursin(carts[c].direction, "><")
					carts[c].direction = turnLeft[carts[c].direction]
				else 
					carts[c].direction = turnRight[carts[c].direction]
				end
			elseif token == "\\"
				if occursin(carts[c].direction, "><")
					carts[c].direction = turnRight[carts[c].direction]
				else
					carts[c].direction = turnLeft[carts[c].direction]
				end
			end
			# now just move forwards
			newPos = carts[c].coords.+directions[carts[c].direction] 
			currentCoords = [e.coords for e in carts]
			if newPos in currentCoords
				println("We collided! Time: ", time)
				idxCollision = findfirst(x -> x==newPos, currentCoords)
				carts[idxCollision].coords = [0, 0] # indicate that the cart has been removed
				carts[c].coords = [0, 0]
				numCarts -= 2
			else 
				carts[c].coords = newPos
			end
		end
		if numCarts == 1
			currentCoords = filter(x-> x!=[0, 0], [e.coords for e in carts])
			println(currentCoords)
			return
		end
		time += 1
	end
end

rails, carts = parseInput(filename)
pushCarts(rails, carts)

