import hashlib

START = "pgflpeqp"
x_max = 3
y_max = 3

def get_door_options(seed):
	algorithm = hashlib.md5()
	algorithm.update(START + seed)
	seed = algorithm.hexdigest()
	return str(seed)[:4]

def get_move_options(code):
	opt = ['U', 'D', 'L', 'R']
	for idx in range(4):
		if code[idx] in 'bcdef':
			yield opt[idx]

def path_taker():
	done = False
	# path, x_pos, y_pos
	solutions = []
	options = [["", 0, 0]]
	while len(options) > 0:
		current = options[0]
		code = get_door_options(current[0])
		for option in get_move_options(code):
			if option == "U" and current[2] > 0:
				# move up
				path = current[0] + option 
				options.append([path, current[1], current[2] - 1])
			elif option == "D" and current[2] < y_max:
				# move down
				path = current[0] + option 
				if current[1] + current[2] + 1 == 6:
					print "Found solution", path 
					solutions.append(len(path))
					#return
				else:
					options.append([path, current[1], current[2] + 1])
			elif option == "L" and current[1] > 0:
				# move left 
				path = current[0] + option 
				options.append([path, current[1] - 1, current[2]])
			elif option == "R" and current[1] < x_max:
				# move right
				path = current[0] + option 
				if current[1] + current[2] + 1 == 6:
					print "Found solution", path 
					solutions.append(len(path))
					#return
				else: 	# else added for part 2
					options.append([path, current[1]+1, current[2]])
		options = options[1:]
	print "maximum solution is", max(solutions)

path_taker()
