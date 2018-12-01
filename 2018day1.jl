function readInput(filename::String)
	fd = open(filename, "r")
	input = read(fd, String)
	return input
end 

function getFrequency(data::String)
	info = split(data, "\n")
	frequencies = map(x->parse(Int64,x), info)
	history = []
	total = 0
	done = false
	while !done
		for freq in frequencies
			total += freq
			if in(total, history)
				println("Repeated!")
				println(total)
				return total
			end
			push!(history, total)
		end
		# println(history)
	end
	return total
end

