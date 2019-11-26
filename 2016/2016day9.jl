function readInput(filename::String)
	fd = open(filename, "r")
	input = read(fd, String)
	return input
end 

function getDecompressedLength(data::String)
	done = false
	total = 0
	while !done
		println(data)
		idx_open = findfirst("(", data)
		if idx_open === nothing
			return length(data) + total
		end
		idx_open = idx_open[1]
		idx_close = findnext(")", data, idx_open)[1]
		idx_delim = findnext("x", data, idx_open)[1]
		distance = parse(Int64, data[idx_open+1:idx_delim-1])
		multiple = parse(Int64, data[idx_delim+1:idx_close-1])
		substr = data[idx_close+1:idx_close+distance]
		substr_length = getDecompressedLength(substr) 
		total += (substr_length * multiple)
		if idx_close + distance < length(data)
			data = data[distance+idx_close+1:end]
		else
			done = true
		end
	end
	return total
end


# 11797310779 too low

#println(getDecompressedLength("(27x12)(20x12)(13x14)(7x10)(1x12)A"))