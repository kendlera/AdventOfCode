START = "10001110011110000"
#TARGET_LEN = 272
TARGET_LEN = 35651584

def get_checksum(x_input):
	#print "input", x_input
	checksum = ""
	it = iter(x_input)
	for chunk in it:
		try:
			if chunk == next(it):
				#print "same"
				checksum += '1'
			else:
				#print "different"
				checksum += '0'
		except StopIteration:
			continue
	if (len(checksum) % 2) == 0:
		return get_checksum(checksum)
	return checksum



def get_disk_bits(seed):
	a = seed
	while len(a) < TARGET_LEN:
		# b = a[::-1]  						# reverse a
		# b = bin(b ^ math.pow(2, len(b))-1) 	# xor to flip all the bits

		# ended up just treating it as a string because was struggling to preserve leading 0s
		flip_and_reverse = ['0' if x == '1' else '1' for x in a[::-1]]
		b = ''.join(flip_and_reverse)

		a = a + '0' + b 					# concatonate new start


	print "final amount", a 
	chksum = get_checksum(a[:TARGET_LEN])
	print "checksum", chksum

