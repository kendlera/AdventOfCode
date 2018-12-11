function readInput(filename::String)
	fd = open(filename, "r")
	input = read(fd, String)
	return input
end 

function parseInput(puzzInput::String)
	inputs = split(puzzInput)
	data = map(x->parse(Int64,x), inputs)
	return data
end

mutable struct node
	num_children::Int64
	num_metadata::Int64
	children::Array
	metadata::Array
	nodeValue::Int64
end


function constructTree(data, expected)
	if length(data) == 0
		return node(0, 0, [], []), 0
	end
	# pattern is num_children, num_medatdata, children, metadata
	done = false
	x = 1 # indexer
	nodesChildren = []
	while !done
		item = node(data[x], data[x+1], [], [], 0)
		x += 2
		if item.num_children > 0
			nodeChildren, numConsumed = constructTree(data[x:end], item.num_children)
			item.children = nodeChildren
			x += numConsumed
		end
		item.metadata = data[x:x+(item.num_metadata-1)]
		x += item.num_metadata 
		push!(nodesChildren, item)
		done = (expected == length(nodesChildren))
	end
	return nodesChildren, x-1
end

function sumMetadata(tree)
	total = 0
	for elem in tree 
		if length(elem.metadata) > 0
			total += sum(elem.metadata)
		end
		for child in elem.children
			total += sumMetadata(child)
		end
	end
	return total
end

function calculateValues(tree)
	for child in tree.children
		calculateValues(child)
	end
	if length(tree.children) == 0 
		if length(tree.metadata) > 0
			tree.nodeValue = sum(tree.metadata)
		end
	else 
		total = 0 
		# println(tree.children)
		for item in tree.metadata 
			if item > length(tree.children)
				continue
			end
			total += tree.children[item].nodeValue 
		end
		tree.nodeValue = total
	end
	return tree
end

# println(sumMetadata(constructTree(parseInput(readInput(filename)), 1)[1][1]))
# println(calculateValues(constructTree(parseInput(readInput(filename)), 1)[1][1]))

