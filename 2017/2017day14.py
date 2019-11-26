from my2017day10 import algorithm


def elim_region(rows, row, col):
	queue = [str(row) + "," + str(col)]
	while len(queue) > 0:
		check = queue[0] 
		queue = queue[1:]
		r, c = check.split(',')
		r = int(r)
		c = int(c)
		rows[r] = rows[r][:c] + "0" + rows[r][c+1:]
		if r > 0:
			if rows[r-1][c] == '1': 
				queue.append(str(r-1) + ',' + str(c))
		if r < 127:
			if rows[r+1][c] == '1':
				queue.append(str(r+1) + ',' + str(c))
		if c > 0:
			if rows[r][c-1] == '1':
				queue.append(str(r) + ',' + str(c-1))
		if c < 127:
			if rows[r][c+1] == '1':
				queue.append(str(r) + ',' + str(c+1)) 
	return rows


def count_regions(rows):
	num_found = 0 
	done = False 
	while not done:
		found = False
		for row in range(len(rows)):
			if '1' in rows[row]:
				col = 0
				for elem in range(len(rows[row])):
					if rows[row][elem] == '1':
						col = elem 
						break
				found = True 
				num_found += 1
				rows = elim_region(rows, row, col)
				break
		done = not found 
	print("Total Regions:", num_found)


def main():
	key = "jzgqcdpd"
	total = 0
	new_rows = []
	for row in range(128):
		puzzle_input = key + "-" + str(row)
		result = algorithm(puzzle_input)
		print(result)
		bins = ""
		for elem in result:
			#print(elem)
			bin_repr = bin(int(elem, 16))[2:]
			if len(bin_repr) < 4:
				filler = '0' * (4 - len(bin_repr)) 
				bin_repr = filler + bin_repr
			bins += bin_repr
		print(bins)
		new_rows.append(bins)
		for num in bins:
			if num == '1': total += 1
	count_regions(new_rows)
	print("Total:", total)

main()