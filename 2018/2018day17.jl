mutable struct clayVein
	x::Array
	y::Array 
end

function parseInput(filename)
	# pull out all they range readings from the input
	fd = open(filename, "r")
	input = read(fd, String)
	items = split(input, "\n")
	veins = []
	for reading in items
		axis1, axis2 = split(reading, ", ")
		value1 = parse(Int64, split(axis1, "=")[2])
		value2, value3 = split(split(axis2, "=")[2], "..")
		value2 = parse(Int64, value2)
		value3 = parse(Int64, value3)
		if string(axis1[1]) == "x"
			vein = clayVein([value1, value1], [value2, value3])
		else 
			vein = clayVein([value2, value3], [value1, value1]) 
		end
		push!(veins, vein)
	end
	return veins
end

function createGrid(veins)
	# using the vein readings, create our map
	minx, maxx, miny, maxy = [1000, 0, 1000, 0]
	# get the range of our graph 
	for v in veins
		minx = (v.x[1] < minx) ? v.x[1] : minx
		maxx = (v.x[2] > maxx) ? v.x[2] : maxx
		miny = (v.y[1] < miny) ? v.y[1] : miny
		maxy = (v.y[2] > maxy) ? v.y[2] : maxy
	end
	println("X range: (", minx, ", ", maxx, ")")
	println("Y range: (", miny, ", ", maxy, ")")
	xshift = minx - 2
	println("Shifting readings over by ", xshift)
	xrange = maxx - (minx - 4)
	println("X range: ", xrange)
	grid = fill(".", maxy+1, xrange)
	for v in veins 
		for xval=v.x[1]:v.x[2] 
			for yval=v.y[1]:v.y[2]
				grid[yval, (xval - xshift)] = "#"
			end
		end
	end
	println("Constructed grid!")
	return grid 
end

function propogateWater(grid)
	# spring is at x=500, y=0
	xshift = 249
	spring = 500 - xshift
	grid[1, spring] = "|"
	# water cannot travel up!
	yrange, xrange = size(grid)
	falling = [[1, spring]]
	done = false
	for y=20:50 
		row = join(grid[y, :][200:300])
		println(row)
	end
	# return
	while !done
		if length(falling) == 0
			println("No more coordinates!")
			break
		end
		current = copy(falling[1])
		grid[current[1], current[2]] = "x"
		for y=20:50 
			row = join(grid[y, :][200:300])
			println(row)
		end
		println("Falling from (", current[1], ", ", current[2], ")")
		hitBottom = false
		while !hitBottom
			if (current[1] + 1) > yrange
				falling = falling[2:end]
				# println("Remaining: ", falling)
				break
			end
			token = grid[current[1]+1, current[2]]
			if token == "."
				# sand
				grid[current[1], current[2]] = "|"
				current[1] += 1 
			elseif token == "|"
				current[1] += 1
			elseif occursin(token, "~#")
				# water or a clay vein 
				hitBottom = true 
				grid[current[1], current[2]] = "|"
				println("Hit bottom at ", current)
			end
		end
		if !hitBottom
			continue
		end
		# now we extend to the sides
		hitLeft = false
		hitRight = false
		left_offset = 1
		while !hitLeft
			token = grid[current[1], current[2]-left_offset]
			if token == "."
				if grid[current[1]+1, current[2]-left_offset] == "."
					# sand underneath!
					push!(falling, [current[1], current[2]-left_offset])
					println("Falling at (", current[1], ", ", current[2]-left_offset, ")")
					break
				end 
			elseif token == "#"
				hitLeft = true
				break
			end
			left_offset += 1
		end 
		right_offset = 1
		while !hitRight
			token = grid[current[1], current[2]+right_offset]
			if token == "."
				if grid[current[1]+1, current[2]+right_offset] == "."
					# sand underneath!
					push!(falling, [current[1], current[2]+right_offset])
					println("Falling at (", current[1], ", ", current[2]+right_offset, ")")
					break
				end 
			elseif token == "#"
				hitRight = true
				break
			end
			right_offset += 1
		end 
		token = (hitLeft && hitRight) ? "~" : "|"
		if token == "|"
			falling = falling[2:end]
			# println("Remaining: ", falling)
		end
		for xfill=current[2]-(left_offset-1):current[2]+(right_offset-1)
			grid[current[1], xfill] = token
		end
		# for y=1:yrange 
		# 	row = join(grid[y, :])
		# 	println(row)
		# end
	end
	return grid 
end

function countWater(grid)
	yrange, xrange = size(grid)
	total = 0
	for y=1:yrange
		for x = 1:xrange
			if occursin(grid[y, x], "~|")
				total += 1 
			end 
		end 
	end 
	println("Total water: ", total)
end 

filename = "/Users/akendler/Documents/personal/AdventofCode/input.txt"
countWater(propogateWater(createGrid(parseInput(filename))))