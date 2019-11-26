using Plots
unicodeplots()

function parseInput(filename)
	fd = open(filename, "r")
	input = read(fd, String)
	inputs = split(input, "\n")
	coordinates = []
	for elem in inputs
		pos, vel = split(elem, "> velocity=<")
		pos = pos[11:end]
		x, y = split(pos, ", ")
		x = parse(Int64, x)
		y = parse(Int64, y)
		vel = vel[1:end-1]
		velx, vely = split(vel, ", ")
		velx = parse(Int64, velx)
		vely = parse(Int64, vely)
		push!(coordinates, [[x, y], [velx, vely]])
	end
	return coordinates
end

function guessStars(coordinates)
	# lets assume that the "winning" solution will have the smallest area
	lastMin = 11990177491
	done = false
	iters = 0
	while !done
		points = [c[1] for c in coordinates]
		xs = [p[1] for p in points]
		ys = [p[2] for p in points]
		boxArea = (maximum(xs) - minimum(xs)) * (maximum(ys) - minimum(ys))
		if boxArea > lastMin
			final = []
			# undo because we've gone one too far
			for x = 1:length(coordinates)
				newPoint = coordinates[x][1].-coordinates[x][2]
				push!(final, newPoint)
			end
			xs = [p[1] for p in final]
			ys = [p[2] for p in final]
			pl = scatter(xs, ys)
			display(pl)
			println("Found in ", iters, " rounds")
			return
		else
			lastMin = boxArea
		end
		moved = []
		for x = 1:length(coordinates)
			newPoint = coordinates[x][1].+coordinates[x][2]
			push!(moved, [newPoint, coordinates[x][2]])
		end
		coordinates = moved
		iters += 1
	end
end

guessStars(parseInput(filename))
