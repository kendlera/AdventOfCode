import Dates

function readInput(filename::String)
	fd = open(filename, "r")
	input = read(fd, String)
	return input
end 

function sortReport(puzzInput::String)
	data = split(puzzInput, "\n")
	reports = []
	for entry in data
		date, report = split(entry, "] ")
		date_obj = Dates.DateTime(replace(date[2:end], " " => "T"))
		push!(reports, [date_obj, report])
	end
	# sort by DateTime
	return sort(reports, by = x->x[1])
end

function findSleepiestGuard(reports::Array)
	sleepTime = Dict()
	# assumes the reports have been sorted
	currentGuard = ""
	start = nothing
	for report in reports
		# println(report)
		if occursin("Guard", report[2])
			currentGuard = split(report[2])[2]
		elseif occursin("asleep", report[2])
			start = report[1]
		elseif occursin("wakes", report[2])
			time_asleep = Dates.value(convert(Dates.Minute, Dates.Period(report[1] - start)))
			sleepTime[currentGuard] = get(sleepTime, currentGuard, 0) + time_asleep
		end
	end
	orderedSleepy = sort(collect(sleepTime), by = tuple -> last(tuple), rev=true)
	return orderedSleepy
end

function findMostSleptTime(reports::Array, chosenGuard::String)
	times = zeros(Int64, 60)
	count = false
	start = 0
	for report in reports
		if occursin("Guard", report[2]) && split(report[2])[2] == chosenGuard
			count = true
		elseif occursin("Guard", report[2])
			count = false
		elseif count && occursin("asleep", report[2])
			start = Dates.minute(report[1])
		elseif count && occursin("wakes", report[2])
			for x = start+1:Dates.minute(report[1])
				times[x] += 1
			end
		end
	end
	max_val = maximum(times)
	index = findfirst(isequal(max_val), times)
	println(chosenGuard, " slept ", max_val, " on minute ", index)
	return index
end

g = findSleepiestGuard(sortReport(readInput("/Users/akendler/Documents/personal/AdventofCode/input.txt")))
println(g)
findMostSleptTime(sortReport(readInput("/Users/akendler/Documents/personal/AdventofCode/input.txt")), "#2593")
