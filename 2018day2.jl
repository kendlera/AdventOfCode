function readInput(filename::String)
	fd = open(filename, "r")
	input = read(fd, String)
	return input
end 

function calcHash(puzzInput::String)
	data = split(puzzInput, "\n")
	hasTwo = 0
	hasThree = 0
	for boxID in data
		found = [false, false]
		for idx in collect(StepRange(1, 1, 25))
			numFound = count(c -> c == boxID[idx], collect(boxID))
			if numFound == 2 && !found[1]
				hasTwo += 1
				found[1] = true
			elseif numFound == 3 && !found[2]
				hasThree += 1
				found[2] = true
			end
			if found[1] && found[2]
				break
			end
		end
	end
	hash = hasTwo * hasThree
	return hash
end

function filterDiff(ans1, ans2)
	same = ""
	for idx in collect(StepRange(1, 1, 25))
		if ans1[idx] == ans2[idx]
			same = same * ans1[idx]
		end
	end
	return same
end

function getDiff(puzzInput::String)
	contenders = []
	data = sort(split(puzzInput, "\n"))
	vectorIDs = map(x->Vector{UInt8}(x), data)
	numIDs = length(data)
	for idx1 in collect(StepRange(1, 1, numIDs-1))
		for idx2 in collect(StepRange(idx1+1, 1, numIDs))
			diff = xor.(vectorIDs[idx1], vectorIDs[idx2])
			filt = filter(x->x!=0x00, diff)
			if length(filt) == 1
				return filterDiff(data[idx1], data[idx2])
			end
		end
	end
end

