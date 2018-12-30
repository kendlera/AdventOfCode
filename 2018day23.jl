struct nanobot
	pos::Array
	radius::Int64
end

function parseInput(filename)
	fd = open(filename, "r")
	input = read(fd, String)
	items = split(input, "\n")
	bots = []
	for line in items
		elem1, elem2 = split(line, ", ")
		rad = parse(Int64, elem2[3:end])
		nums = split(elem1[6:end-1], ",")
		points = []
		for n in nums
			p = parse(Int64, n)
			push!(points, p)
		end 
		b = nanobot(points, rad)
		push!(bots, b)
	end 
	return bots
end

function withinRange(source, options)
	total = 0 
	for bot in options
		print(bot)
		dist = abs(source.pos[1] - bot.pos[1]) + abs(source.pos[2] - bot.pos[2]) + abs(source.pos[3] - bot.pos[3])
		println(",  Distance: ", dist)
		if dist <= source.radius 
			total += 1
		end
	end  
	return total 
end

function naiveApproach(bots)
	x_bots = sort!(bots, by=x->x.pos[1])
	xshift = abs(x_bots[1].pos[1]) + 1
	xmax = x_bots[end].pos[1]
	y_bots = sort!(bots, by=x->x.pos[2])
	yshift = abs(y_bots[1].pos[2]) + 1
	ymax = y_bots[end].pos[2]
	z_bots = sort!(bots, by=x->x.pos[3])
	zshift = abs(z_bots[1].pos[3]) + 1
	zmax = z_bots[end].pos[3]
	println("Ranges: (", 1-xshift, ", ", xmax, ") (", 1-yshift, ", ", ymax, ") (", 1-zshift, ", ", zmax, ")")
	println("Size: ", xshift+xmax, " x ", yshift+ymax, " x ", zshift+zmax)
	space = zeros(xshift+xmax+10, yshift+ymax+10, zshift+zmax+10)
	xrange, yrange, zrange = size(space)
	ops = [+, -]
	for bot in bots 
		println("Evaluating for ", bot)
		for x_offset=0:bot.radius
			println("Evaluating x_offset ", x_offset)
			for y_offset=0:(bot.radius - x_offset)
				for z_offset=0:bot.radius - (x_offset+y_offset)
					xpos = bot.pos[1] + xshift
					ypos = bot.pos[2] + yshift
					zpos = bot.pos[3] + zshift
					# println("x: ", x_offset, ", y: ", y_offset, ", z: ", z_offset)
					xend = x_offset > 0 ? 2 : 1
					yend = y_offset > 0 ? 2 : 1
					zend = z_offset > 0 ? 2 : 1
					for xop=1:xend
						for yop=1:yend
							for zop=1:zend
								xval = ops[xop](xpos, x_offset)
								yval = ops[yop](ypos, y_offset)
								zval = ops[zop](zpos, z_offset)
								try
									space[xval, yval, zval] += 1
								catch e 
									# do nothing! we've tried to access outside our bounds
								end
							end
						end 
					end
				end 
			end 
		end 
	end
	num, ans = findmax(space)
	println("Has ", num, " bots")
	println("(", ans[1]-xshift, ", ", ans[2]-yshift, ", ", ans[3]-zshift, ")")
	# println(space)
end 


using LightGraphs, SimpleWeightedGraphs

function areOverlapping(bot1, bot2)
	dist = abs(bot1.pos[1] - bot2.pos[1]) + abs(bot1.pos[2] - bot2.pos[2]) + abs(bot1.pos[3] - bot2.pos[3])
	return (dist <= (bot1.radius + bot2.radius))
end

function nanobotTouches(bot, point)
	dist = abs(bot.pos[1] - point[1]) + abs(bot.pos[2] - point[2]) + abs(bot.pos[3] - point[3])
	return (dist < bot.radius)
end

function shiftPoint(sourcePoint, destPoint, distance)
	# find the point 'distance' from sourcePoint in the direction of destPoint
	uvector = [destPoint[1] - sourcePoint[1], destPoint[2] - sourcePoint[2], destPoint[3] - sourcePoint[3]]
	usize = sqrt((uvector[1]^2) + (uvector[2]^2) + (uvector[3]^2))
	norm_uvector = [uvector[1]/usize, uvector[2]/usize, uvector[3]/usize]
	expanded_vect = [round(norm_uvector[1]*distance),  round(norm_uvector[2]*distance), round(norm_uvector[3]*distance)]
	point = expanded_vect.+sourcePoint
	return point 
end

function numFailToTouch(point, candidates)
	distances = []
	for bot in candidates 
		if !nanobotTouches(bot, point)
			# println("Issue! ", bot)
			dist_from_center = abs(bot.pos[1] - point[1]) + abs(bot.pos[2] - point[2]) + abs(bot.pos[3] - point[3])
			dist_from_border = dist_from_center - bot.radius
			push!(distances, dist_from_border)
			# println("Off by: ", dist_from_border)
		end 
	end
	numBots = length(distances)
	if numBots == 0 
		return 0, 0
	end
	return length(distances), sum(distances)
end

function findOverlapping(bots)
	overlapping = SimpleWeightedGraph(length(bots))
	for src=1:length(bots)
		println("Evaluating pairs for nanobot ", src)
		for dst=src+1:length(bots)
			if areOverlapping(bots[src], bots[dst])
				add_edge!(overlapping, src, dst)
			end 
		end 
	end
	cliques = maximal_cliques(overlapping)
	clique = []
	maxc = 0
	for c in cliques
		lenc = length(c)
		if lenc > maxc 
			maxc = lenc
			clique = c
		end
	end 
	numPoints = length(clique)
	println("Size of Max. Clique: ", numPoints)
	candidates = []
	avgx, avgy, avgz = [0, 0, 0]
	for i in clique
		avgx += bots[i].pos[1]
		avgy += bots[i].pos[2]
		avgz += bots[i].pos[3]
		push!(candidates, bots[i])
	end 
	point = [floor(avgx/numPoints), floor(avgy/numPoints), floor(avgz/numPoints)]
	println("Average point: ", point)
	# total = abs(point[1]) + abs(point[2]) + abs(point[3])
	# println("Distance: ", total)
	perfect = false
	attemptNum = 1
	jump_size = 1000
	while !perfect
		# println(point)
		numMissing, totaldist = numFailToTouch(point, candidates)
		if numMissing == 0 
			perfect = true
			break 
		else
			# println(numMissing, " nanobots fail to touch the point")
		end
		# figure out in which direction we can move the point
		ops = [+, -]
		data = []
		lastDist = totaldist
		for xop in ops 
			npoint = copy(point)
			npoint[1] = xop(npoint[1], jump_size)
			numMissing, totaldist = numFailToTouch(npoint, candidates)
			push!(data, [npoint, numMissing, totaldist])
			# println(numMissing, " nanobots fail to touch the point by a total dist of ", totaldist)
		end 
		for yop in ops 
			npoint = copy(point)
			npoint[2] = yop(npoint[2], jump_size)
			numMissing, totaldist = numFailToTouch(npoint, candidates)
			push!(data, [npoint, numMissing, totaldist])
			# println(numMissing, " nanobots fail to touch the point by a total dist of ", totaldist)
		end 
		for zop in ops 
			npoint = copy(point)
			npoint[3] = zop(npoint[3], jump_size)
			numMissing, totaldist = numFailToTouch(npoint, candidates)
			push!(data, [npoint, numMissing, totaldist])
			# println(numMissing, " nanobots fail to touch the point by a total dist of ", totaldist)
		end
		best = sort!(data, by=x->x[3])[1]
		if best[3] > lastDist
			# we probably overshot! halve the jump_dist and keep going 
			jump_size = floor(jump_size/2)
			if jump_size == 0 
				jump_size = 1
			end
		else 
			point = best[1]
		end
		attemptNum += 1
		if attemptNum == 900000 
			break
		elseif attemptNum % 1000 == 0
			println(point, " not touched by ", best[2], " bots and is net ", best[3], " distance away.")
			if best[2] == 4  	# break out here because we're stuck
				println("Total: ", sum(point)) 
				return
			end
		end
		#= sdist = sort!(distances, by=x->x[1])
		destDist, destPoint = sdist[end]
		# we want to shift 'point' towards the furthest sphere
		point = shiftPoint(copy(point), copy(destPoint.pos), destDist) =#
	end
	if perfect 
		println("We did it!")
	else 
		println("Failed")
		return
	end
	println(point, ": ", sum(point))
	# we now have a point within the region overlapped by all nanobots. Gradually move towards the origin until we fail?
	lastTrue = copy(point)
	stillTouching = true
	while stillTouching
		point = shiftPoint(copy(point), [0, 0, 0], 1)
		for bot in candidates 
			if !nanobotTouches(bot, point)
				println(point, " is not touched by ", bot)
				stillTouching = false
				break
			end 
		end
		println(point, ": ", sum(point))
		if stillTouching
			lastTrue = point 
		end 
	end
	println(lastTrue, ": ", sum(lastTrue))
end

bots = parseInput(filename)
# @time naiveApproach(bots)
@time findOverlapping(bots)



# sorted_bots = sort!(bots, by=x->x.radius, rev=true)
# strongest = sorted_bots[1]
# others = bots[2:end]
# numValid = withinRange(strongest, others)