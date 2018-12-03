function readInput(filename::String)
	fd = open(filename, "r")
	input = read(fd, String)
	return input
end 

function processCutRequests(puzzInput::String)
	data = split(puzzInput, "\n")
	fabric = zeros(Int64, 1001, 1001)
	total = 0
	for suggestion in data
		id, dimens = split(suggestion, " @ ")
		location, size = split(dimens, ": ")
		startx, starty = split(location, ",")
		distx, disty = split(size, "x")
		starty = parse(Int64, starty)
		startx = parse(Int64, startx)
		distx = parse(Int64, distx)
		disty = parse(Int64, disty)
		for y = starty:starty+disty-1
			for x = startx:startx+distx-1
				fabric[x+1,y+1] += 1
				if fabric[x+1, y+1] == 2
					total += 1
				end
			end
		end
	end
	return total
end

function findSafePattern(puzzInput::String)
	data = split(puzzInput, "\n")
	fabric = zeros(Int64, 1001, 1001)
	total = 0
	valid = []
	for suggestion in data
		id, dimens = split(suggestion, " @ ")
		id = parse(Int64, id[2:end])
		location, size = split(dimens, ": ")
		startx, starty = split(location, ",")
		distx, disty = split(size, "x")
		starty = parse(Int64, starty)
		startx = parse(Int64, startx)
		distx = parse(Int64, distx)
		disty = parse(Int64, disty)
		overlap = false
		for y = starty:starty+disty-1
			for x = startx:startx+distx-1
				currentVal = fabric[x+1,y+1]
				if currentVal == 0
					fabric[x+1,y+1] = id
				else
					overlap = true
					if currentVal in valid
						filter!(x->x != currentVal, valid)
					end
				end
			end
		end
		if !overlap
			push!(valid, id)
		end
	end
	return valid
end
