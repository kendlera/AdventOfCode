function readInput(filename::String)
	fd = open(filename, "r")
	input = read(fd, String)
	return input
end 

function parseInput(puzzInput::String)
	data = split(puzzInput, "\n")
	instructions = Dict()
	for req in data
		s, first, m, b, f, be, st, later, c, beg = split(req, " ") 
		instructions[later] = push!(get(instructions, later, []), first)
	end
	return instructions
end

function orderSteps(instructions)
	defaultOrder = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	actualOrder = ""
	while length(actualOrder) != length(defaultOrder)
		for step in defaultOrder
			if step in actualOrder
				# we have already done this step
				continue
			end
			prerequisites = get(instructions, string(step), [])
			remaining = filter(x->!occursin(x, actualOrder), prerequisites)
			if length(remaining) == 0
				actualOrder = (actualOrder*step)
				break
			end
		end
	end
	return actualOrder
end

function chooseJob(remaining, completed, dependencies)
	defaultOrder = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for step in defaultOrder
		if !occursin(step, remaining)
			continue
		end
		ready = true
		prerequisites = get(dependencies, string(step), [])
		for prerequisite in prerequisites
			# check if prereqs are fulfilled
			if !occursin(prerequisite, completed)
				ready = false
				break
			end
		end
		if ready
			return step 
		end
	end
	return 0
end

function doSteps(workOrder::String, dependencies, numWorkers)
	completed = ""
	elapsedTime = 0
	done = false
	workersTime = zeros(Int64, numWorkers)
	workersJobs = fill(".", numWorkers)
	while !done
		for worker=1:numWorkers
			if workersTime[worker] == 0
				if workersJobs[worker] != "."
					# the previous job is done
					completed = (completed*workersJobs[worker])
					workersJobs[worker] = "."
				end
			end
		end
		for worker=1:numWorkers
			if workersTime[worker] == 0
				# can do a new job
				if length(workOrder) == 0
					workersTime[worker] = 1 # cheat so we'll decrement it back to 0
					continue
				end
				nextJob = chooseJob(workOrder, completed, dependencies)
				if nextJob == 0
					# no valid jobs
					workersTime[worker] = 1 # cheat so we'll decrement it back to 0
					continue
				end
				workOrder = filter(x->x!=nextJob, workOrder)
				# println("Time ", elapsedTime,  ": Starting Worker ", worker, " on step ", nextJob, " for ", (60 + (Int(nextJob) - 64)), " seconds")
				workersJobs[worker] = string(nextJob)
				workersTime[worker] = (60 + (Int(nextJob) - 64))
			end
		end
		workersTime = workersTime.-1
		if length(completed) == 26
			done = true
			return elapsedTime
		end
		elapsedTime += 1
	end
	return elapsedTime
end

dependencies = parseInput(readInput(filename))
@time workOrder = orderSteps(dependencies)
@time timeSpent = doSteps(workOrder, dependencies, 5)
println(timeSpent)
