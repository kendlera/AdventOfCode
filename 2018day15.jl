using DataStructures
using Printf 

function parseInput(filename)
	# rename 'G' to generic letter
	goblinNames = "ABCDFHIJKLMNOPQRSTUVWXYZ"
	gIdx = 1
	elfNames = "0123456789"
	eIdx = 1
	# rename 'E' to number
	hit_points = Dict()
	fd = open(filename, "r")
	input = read(fd, String)
	board = split(input, "\n")
	for line=1:length(board)
		done = false
		while !done
			goblin = findfirst("G", board[line])
			if goblin != nothing
				name = string(goblinNames[gIdx])
				gIdx += 1
				hit_points[name] = 200 
				board[line] = board[line][1:goblin[1]-1] * name * board[line][goblin[1]+1:end]
			end
			elf = findfirst("E", board[line])
			if elf != nothing
				name = string(elfNames[eIdx])
				eIdx += 1
				hit_points[name] = 200 
				board[line] = board[line][1:elf[1]-1] * name * board[line][elf[1]+1:end]
			end
			if goblin == nothing && elf == nothing
				done = true
			end
		end
	end
	return board, hit_points
end

function buildPath(boardDists, start, target)
	# go from target to start, preferring 'read-order'
	# @printf("Building path from (%d, %d) to (%d, %d)\n", start[1], start[2], target[1], target[2])
	# show(stdout, "text/plain", boardDists)
	# println()
	# println()
	# return
	pathToTarget = [target]
	current = target 
	done = false
	timer = 0
	while !done
		x, y = current
		minDist = 100
		if (boardDists[y-1, x] < minDist)
			next = [x, y-1]
			minDist = boardDists[y-1, x]
		end
		if (boardDists[y, x-1] < minDist)
			next = [x-1, y]
			minDist = boardDists[y, x-1]
		end 
		if (boardDists[y, x+1] < minDist)
			next = [x+1, y]
			minDist = boardDists[y, x+1]
		end
		if (boardDists[y+1, x] < minDist)
			next = [x, y+1]
			minDist = boardDists[y+1, x]
		end
		if minDist == 100
			println("Error! we should have found a closer neighbor")
			println(boardDists)
		end 
		# @printf("Choosing (%d, %d) as our next step\n", next[1], next[2])
		current = next
		if next[1] == start[1] && next[2] == start[2]
			done = true
		else
			push!(pathToTarget, next)
		end
	end
	return reverse(pathToTarget)
end

function findClosestTarget(board, xcoord, ycoord, targetType)
	goblinNames = "ABCDFHIJKLMNOPQRSTUVWXYZ"
	elfNames = "0123456789"
	target = ""
	boardDists = fill(100, length(board[1]), length(board))
	# println("Evaluating for ", board[ycoord][xcoord], " at ", xcoord, ", ", ycoord)
	boardDists[ycoord, xcoord] = 0
	# println("Setting ", ycoord, ", ", xcoord, " to 0")
	stop = false
	points = Queue{String}()
	enqueue!(points, string(xcoord) * "," * string(ycoord-1))
	enqueue!(points, string(xcoord-1) * "," * string(ycoord))
	enqueue!(points, string(xcoord+1) * "," * string(ycoord))
	enqueue!(points, string(xcoord) * "," * string(ycoord+1))
	while !isempty(points)
		current = dequeue!(points)
		x, y = split(current, ",")
		x = parse(Int64, x)
		y = parse(Int64, y)
		token = string(board[y][x])
		if token == "#" || (occursin(token, goblinNames) && targetType == "E") || (occursin(token, elfNames) && targetType == "G")
			# this is something we have to go around 
			# do nothing
			boardDists[y, x] = 101
		elseif token == "."
			# this is an open square 
			minNeighbor = 100
			if boardDists[y-1, x] < minNeighbor
				minNeighbor = boardDists[y-1, x]
			end
			if boardDists[y, x-1] < minNeighbor
				minNeighbor = boardDists[y, x-1]
			end
			if boardDists[y, x+1] < minNeighbor
				minNeighbor = boardDists[y, x+1]
			end
			if boardDists[y+1, x] < minNeighbor
				minNeighbor = boardDists[y+1, x]
			end
			if minNeighbor == 100
				println("Error? We should have found a lower neighbor!")
				return
			end
			boardDists[y, x] = minNeighbor+1
			if !stop 
				neighbor = string(x+1) * "," * string(y)
				val = boardDists[y, x+1]
				if (val == 100) && !(neighbor in points)
					enqueue!(points, neighbor)
				end
				neighbor = string(x-1) * "," * string(y)
				val = boardDists[y, x-1]
				if (val == 100) && !(neighbor in points)
					enqueue!(points, neighbor)
				end
				neighbor = string(x) * "," * string(y-1)
				val = boardDists[y-1, x]
				if (val == 100) && !(neighbor in points)
					enqueue!(points, neighbor)
				end
				neighbor = string(x) * "," * string(y+1)
				val = boardDists[y+1, x]
				if (val == 100) && !(neighbor in points)
					enqueue!(points, neighbor)
				end
			end
		elseif !stop 
			# this is a valid target!
			# println("Found a target at ", x, ", ", y, ": ", token)
			target = [x, y]
			stop = true # we still want to process what's in our queue but we indicate we should stop adding to it
		end
	end
	if !stop 
		# we never found a valid target!
		return [] 
	end
	return buildPath(boardDists, [xcoord, ycoord], target)
end

function calculateAnswer(rounds, hit_points)
	health = sum(values(hit_points))
	ans = health * rounds 
	println(rounds, " x ", health, " = ", ans)
	return ans
end

function projectCombat(board, hit_points, attack_power)
	goblinNames = "ABCDFHIJKLMNOPQRSTUVWXYZ"
	elfNames = "0123456789"
	rounds = 0
	done = false
	while !done
		hasMoved = []
		for y=1:length(board)
			for x=1:length(board[1])
				name = string(board[y][x])
				if !occursin(name, "#.") && !(name in hasMoved)
					# we must make a move
					push!(hasMoved, name)
					targetType = "E"
					if occursin(name, elfNames)
						# it's an elf
						targetType = "G"
					end
					pathToTarget = findClosestTarget(board, x, y, targetType)
					dist = length(pathToTarget)
					if dist == 0 
						# either the battle is over, or all targets are surrounded
						println(name, " cannot make any moves")
						fighting = false
						if occursin(name, elfNames)
							for i=1:length(goblinNames)
								if haskey(hit_points, string(goblinNames[i]))
									fighting = true
									break
								end
							end
						else
							for i=1:length(elfNames)
								if haskey(hit_points, string(elfNames[i]))
									fighting = true 
									break 
								end
							end
						end
						if !fighting
							# we're done!
							return calculateAnswer(rounds, hit_points)
						end
						continue
					elseif dist > 1
						# we should move 
						board[y] = board[y][1:x-1] * "." * board[y][x+1:end]
						nextx, nexty = pathToTarget[1]
						println(name, " is moving to ", pathToTarget[1])
						board[nexty] = board[nexty][1:nextx-1] * name * board[nexty][nextx+1:end]
						myx = nextx 
						myy = nexty 
					else 
						myx = x 
						myy = y
					end
					# we should attack if possible
					target = []
					minHealth = 1000
					if (targetType == "E" && occursin(board[myy-1][myx], elfNames)) ||  (targetType == "G" && occursin(board[myy-1][myx], goblinNames))
						token = string(board[myy-1][myx])
						target = [myy-1, myx]
						minHealth = hit_points[token]
					end
					if (targetType == "E" && occursin(board[myy][myx-1], elfNames)) ||  (targetType == "G" && occursin(board[myy][myx-1], goblinNames))
						token = string(board[myy][myx-1])
						if hit_points[token] < minHealth
							minHealth = hit_points[token]
							target = [myy, myx-1]
						end
					end
					if (targetType == "E" && occursin(board[myy][myx+1], elfNames)) ||  (targetType == "G" && occursin(board[myy][myx+1], goblinNames))
						token = string(board[myy][myx+1])
						if hit_points[token] < minHealth
							minHealth = hit_points[token]
							target = [myy, myx+1]
						end
					end
					if (targetType == "E" && occursin(board[myy+1][myx], elfNames)) ||  (targetType == "G" && occursin(board[myy+1][myx], goblinNames))
						token = string(board[myy+1][myx])
						if hit_points[token] < minHealth
							minHealth = hit_points[token]
							target = [myy+1, myx]
						end
					end
					if minHealth == 1000
						# we did not find any targets
						continue
					end
					token = string(board[target[1]][target[2]])
					if occursin(name, elfNames)
						targetHealth = minHealth - attack_power
						println("Elf ", board[y][x], " is attacking ", token, " who has ", targetHealth, " hit points")
					else 
						targetHealth = minHealth - 3
						println("Goblin ", board[y][x], " is attacking ", token, " who has ", targetHealth, " hit points")
					end
					if targetHealth <= 0 # we killed it!
						println(board[y][x], " killed ", token)
						if occursin(token, elfNames)
							println("We killed an elf! End the projection.")
							return 0
						end
						delete!(hit_points, token)
						board[target[1]] = board[target[1]][1:target[2]-1] * "." * board[target[1]][target[2]+1:end]
					else
						hit_points[token] = targetHealth
					end
				end
			end
		end
		rounds += 1
		# for i=1:length(board)
		# 	println(board[i])
		# end
		println("Round ", rounds)
	end
end

board, hit_points = parseInput(filename)
for i=1:length(board)
	println(board[i])
end

count = 20
winning = false
for i in 20:5:100
	result = projectCombat(copy(board), copy(hit_points), i)
	if result != 0
		println("Success with power ", i)
		break
	end
end
