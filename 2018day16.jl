mutable struct example 
	before::Array
	after::Array
	command::Array
end

function parseInput(filename)
	fd = open(filename, "r")
	input = read(fd, String)
	items = split(input, "\n\n")
	examples = []
	for i in items
		b, c, a = split(i, "\n")
		b = replace(b, "Before: ["=> "")
		b = replace(b, ","=> "")
		be = []
		for elem in split(b[1:end-1], " ")
			push!(be, parse(Int64, elem))
		end 
		co = []
		for elem in split(c, " ")
			push!(co, parse(Int64, elem))
		end
		a = replace(a, "After:  ["=>"")
		a = replace(a, ","=>"")
		af = []
		for elem in split(a[1:end-1], " ")
			push!(af, parse(Int64, elem))
		end 
		thisExample = example(be, af, co)
		push!(examples, thisExample)
	end
	return examples
end

function parseInput2(filename)
	fd = open(filename, "r")
	input = read(fd, String)
	items = split(input, "\n")
	commands = []
	for i in items
		comm = []
		for elem in split(i, " ")
			push!(comm, parse(Int64, elem))
		end 
		push!(commands, comm)
	end 
	return commands
end 

operators = Dict("add"=>+, "mul"=>*, "ban"=>&, "bor"=>|)
# all op functions should take in a list of registers, and a list with the command sequence
# the function should return a list of registers
function regop(regs, command, opType)
	newRegs = copy(regs)
	op = operators[opType]
	newRegs[command[4]+1] = op(regs[command[2]+1], regs[command[3]+1])
	return newRegs
end
function valop(regs, command, opType)
	newRegs = copy(regs)
	op = operators[opType]
	newRegs[command[4]+1] = op(regs[command[2]+1], command[3])
	return newRegs
end
function setreg(regs, command)
	newRegs = copy(regs)
	newRegs[command[4]+1] = regs[command[2]+1]
	return newRegs 
end
function setval(regs, command)
	newRegs = copy(regs)
	newRegs[command[4]+1] = command[2]
	return newRegs 
end
comparisons = Dict("gt" => >, "eq" => ==)
function ir(regs, command, opType)
	newRegs = copy(regs)
	comp = comparisons[opType]
	newRegs[command[4]+1] = comp(command[2], regs[command[3]+1]) ? 1 : 0 
	return newRegs
end 
function ri(regs, command, opType) 
	newRegs = copy(regs)
	comp = comparisons[opType]
	newRegs[command[4]+1] = comp(regs[command[2]+1], command[3]) ? 1 : 0 
	return newRegs
end 
function rr(regs, command, opType)
	newRegs = copy(regs)
	comp = comparisons[opType]
	newRegs[command[4]+1] = comp(regs[command[2]+1], regs[command[3]+1]) ? 1 : 0 
	return newRegs
end 

function evalTests(examples)
	# total = 0
	opCodes = Dict()
	for item in examples
		itemTotal = []
		opCode = item.command[1]
		for key in ["add", "mul", "ban", "bor"]
			result = regop(item.before, item.command, key)
			push!(itemTotal, result == item.after)
			result = valop(item.before, item.command, key)
			push!(itemTotal, result == item.after)
		end 
		for key in ["gt", "eq"]
			result = ir(item.before, item.command, key)
			push!(itemTotal, result == item.after)
			result = ri(item.before, item.command, key)
			push!(itemTotal, result == item.after)
			result = rr(item.before, item.command, key)
			push!(itemTotal, result == item.after)
		end
		result = setreg(item.before, item.command) 
		push!(itemTotal, result == item.after)
		result = setval(item.before, item.command)
		push!(itemTotal, result == item.after)
		if !haskey(opCodes, opCode)
			opCodes[opCode] = itemTotal 
		else
			current = opCodes[opCode]
			winningVersion = []
			for i=1:length(current)
				push!(winningVersion, current[i] && itemTotal[i]) 
			end 
			opCodes[opCode] = winningVersion
		end
	end
	# println(total)
	options = ["addr", "addi", "mulr", "muli", "banr", "bani", "borr", "bori", "gtir", "gtri", "gtrr", "eqir", "eqri", "eqrr", "setr", "seti"]
	ans = Dict()
	taken = fill(false, length(options))
	done = false
	while !done
		for opCode in keys(opCodes)
			results = opCodes[opCode]
			currentResult = []
			for i=1:length(results)
				push!(currentResult, !taken[i] && results[i]) 
			end 
			if count(isequal(true), currentResult) == 1
				idx = findfirst(isequal(true), currentResult)[1] 
				println(opCode, " corresponds to ", options[idx])
				ans[opCode] = options[idx]
				taken[idx] = true
				delete!(opCodes, opCode)
			end 
		end 
		done = count(isequal(true), taken) == length(taken)
	end 
	println(ans)
	return ans
end

function executeCommands(ans, commands)
	# ans gives us the translation we need 
	regs = fill(0, 4)
	for comm in commands 
		task = ans[comm[1]] 
		println(task, ": ", comm)
		if haskey(operators, string(task[1:3]))
			if string(task[end]) == "r"
				println("Executing regop with operator ", string(task[1:3]))
				regs = regop(regs, comm, string(task[1:3]))
			else
				println("Executing valop with operator ", string(task[1:3]))
				regs = valop(regs, comm, string(task[1:3]))
			end 
		elseif haskey(comparisons, string(task[1:2]))
			token = string(task[3:4])
			if token == "ir"
				println("Executing ir with comparison ", string(task[1:2]))
				regs = ir(regs, comm, string(task[1:2]))
			elseif token == "ri"
				println("Executing ri with comparison ", string(task[1:2]))
				regs = ri(regs, comm, string(task[1:2]))
			else 
				println("Executing rr with comparison ", string(task[1:2]))
				regs = rr(regs, comm, string(task[1:2]))
			end 
		elseif task == "setr"
			println("Executing setreg")
			regs = setreg(regs, comm)
		else 
			println("Executing setval")
			regs = setval(regs, comm)
		end 
		println(regs)
	end 
	println(regs)
end 

examples = parseInput(filename)
commands = parseInput2(filename2)
translation = evalTests(examples)
executeCommands(translation, commands)

