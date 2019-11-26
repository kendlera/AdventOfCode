
function readInput(filename::String)
	fd = open(filename, "r")
	input = read(fd, String)
	return input
end 

function reducePolymer(puzzInput::String)
	lowers = "abcdefghijklmnopqrstuvwxyz"
	uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	matched = [[lowers[x]*uppers[x] for x in 1:26]; [uppers[x]*lowers[x] for x in 1:26]]
	newLen = 1
	currentLen = 100
	while currentLen != newLen
		currentLen = length(puzzInput)
		removeMatch = []
		x = 1
		while x <= currentLen-1
			if puzzInput[x:x+1] in matched
				if !(puzzInput[x:x+1] in removeMatch)
					push!(removeMatch, puzzInput[x:x+1])
				end
				x += 2
			else
				x += 1
			end
		end
		for matches in removeMatch
			puzzInput = replace(puzzInput, matches=>"")
		end
		newLen = length(puzzInput)
	end
	return newLen
end

import Dates
started = Dates.now()
lowers = "abcdefghijklmnopqrstuvwxyz"
uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
results = []
for x = 1:26
	scrubbed = replace(replace(puzzInput, lowers[x]=>""), uppers[x]=>"")
	newLen = reducePolymer(scrubbed)
	push!(results, [newLen, lowers[x]])
end
println(sort!(results, by = x->x[1])[1])
println(convert(Dates.Millisecond, Dates.Period(Dates.now() - started)))
