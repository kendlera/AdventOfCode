
INPUT = "Disc #1 has 13 positions; at time=0, it is at position 11.\nDisc #2 has 5 positions; at time=0, it is at position 0.\nDisc #3 has 17 positions; at time=0, it is at position 11.\nDisc #4 has 3 positions; at time=0, it is at position 0.\nDisc #5 has 7 positions; at time=0, it is at position 2.\nDisc #6 has 19 positions; at time=0, it is at position 17."


def load_input():
	levels = INPUT.split("\n")
	disk_state = []
	for level in levels:
		words = level.split(" ")
		positions = int(words[3])
		current_state = int(words[-1].replace(".", ""))
		disk_state.append([positions, current_state])
	return disk_state


def calculate_answer():
	'''
	we can probably use CRT to find the answer; all the modulos are co-prime!
	just increment starting position according to the time the 
		ball would hit it.

	x1 = 12 mod 13
	x2 = 2  mod 5
	x3 = 14 mod 17
	x4 = 1  mod 3
	x5 = 0  mod 7
	x6 = 4  mod 19

	'''
	states = load_input()

