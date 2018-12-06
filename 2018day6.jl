function readInput(filename::String)
	fd = open(filename, "r")
	input = read(fd, String)
	return input
end 

function parseInput(puzzInput::String)
	data = split(puzzInput, "\n")
	coords = []
	for dest in data
		x, y = split(dest, ", ")
		x = parse(Int64, x)+1
		y = parse(Int64, y)+1
		push!(coords, [x, y])
	end
	return coords 
end

function growField(field, coords)
	dist = 1
	xlen, ylen = size(field)
	while "#" in field
		other_tag =  ":" * string(dist)
		println("Round ", dist)
		for x=1:length(coords)
			tag = ("+" * string(x) * other_tag)
			offset = 0 # we use this to do diagonals
			while offset < dist
				# println("xval: ", coords[x][1]+dist-offset, " yval: ", coords[x][2]-offset)
				# println("value at: ", field[218, 47])
				xval = coords[x][1]+dist-offset 
				yval = coords[x][2]-offset
				if (1 <= xval <= xlen) && (1 <= yval <= ylen) 
					if (field[xval, yval] == "#")
						field[xval, yval] = tag
					elseif occursin(other_tag, field[xval, yval])
						field[xval, yval] = " . "
					end
				end
				xval = coords[x][1]-dist+offset 
				yval = coords[x][2]+offset
				if (1 <= xval <= xlen) && (1 <= yval <= ylen) 
					if (field[xval, yval] == "#")
						field[xval, yval] = tag
					elseif occursin(other_tag, field[xval, yval])
						field[xval, yval] = " . "
					end
				end
				xval = coords[x][1]+offset
				yval = coords[x][2]+dist-offset
				if (1 <= xval <= xlen) && (1 <= yval <= ylen) 
					if (field[xval, yval] == "#")
						field[xval, yval] = tag
					elseif occursin(other_tag, field[xval, yval])
						field[xval, yval] = " . "
					end
				end
				xval = coords[x][1]-offset
				yval = coords[x][2]-dist+offset
				if (1 <= xval <= xlen) && (1 <= yval <= ylen) 
					if (field[xval, yval] == "#")
						field[xval, yval] = tag
					elseif occursin(other_tag, field[xval, yval])
						field[xval, yval] = " . "
					end
				end
				offset += 1
			end
		end
		# this is for printing
		# for row = 1:xlen
		# 	for col= 1:ylen
		# 		print(field[row, col], " ")
		# 	end
		# 	println("")
		# end
		dist += 1
	end
	# let's weed out any points that hit the edge since they're "infinite growers"
	disqualify = []
	for item = 1:xlen
		obj = split(field[item, 1], ":")[1]
		if !(obj in disqualify)
			push!(disqualify, obj)
		end
		obj = split(field[item, end], ":")[1]
		if !(obj in disqualify)
			push!(disqualify, obj)
		end
	end
	for item = 1:ylen
		obj = split(field[1, item], ":")[1]
		if !(obj in disqualify)
			push!(disqualify, obj)
		end
		obj = split(field[end, item], ":")[1]
		if !(obj in disqualify)
			push!(disqualify, obj)
		end
	end
	pairwise = []
	for x=1:length(coords)
		if ("+"*string(x)) in disqualify
			continue
		end
		tag = ("+" * string(x) * ":")
		# println(tag)
		area = length(findall(x->occursin(tag, x), field))
		push!(pairwise, [x, area])
		println("Coordinate ", x, " grew to an area of ", area)
	end
	println(sort!(pairwise, by = x->x[2], rev=true))
end

function populateField(puzzInput::String)
	coords = sort!(parseInput(puzzInput), by=x->x[1])
	adjusted_coords = []
	minx = coords[1][1] - 1
	maxx = coords[end][1]
	ycoords = sort!(coords, by=x->x[2])
	miny = ycoords[1][2] - 1
	maxy = ycoords[end][2]
	field = fill("#", maxx-minx+5, maxy-miny+5)
	for x=1:length(coords)
		# println("original: ", coords[x], "new: [", coords[x][1]-(minx), ", ", coords[x][2]-(miny), "]")
		field[coords[x][1]-(minx), coords[x][2]-(miny)] = ("+" * string(x) * ":0")
		push!(adjusted_coords, [coords[x][1]-(minx), coords[x][2]-(miny)])
	end
	growField(field, adjusted_coords)
end

function getDist(coord1, coord2)
	return abs(coord1[1] - coord2[1]) + abs(coord1[2] - coord2[2])
end

@time populateField(readInput("/Users/akendler/Documents/personal/AdventofCode/input.txt"))
