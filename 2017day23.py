b = (79 * 100) + 100000 
c = b + 17000
'''
done = False
# this loop will be done 1000 times
while not done:
	f = 1
	d = 2
	# here is our other loop
	e = 2
	g = (d*e) - b 
	if g == 0:
		f = 0
	e += 1
	g = (e-b)
	if g == 0:
		if f == 0:
			h += 1 
		d += 1
		g = (b-c)
		if (g == 0):
			print("DONE: h = {}".format(h)) 
			done = True
		else:
			b += 17

b = 107900 
c = 109600 
d = 2
h = 0
while b != c:
	# if d is a multiple of b, increment b
	if (b ) == 0:
		h += 1 
	d += 1 
	b += 17
print("h: {}".format(h))
'''

# if b is an even number, we will increment h 

# guessed 500; wrong

# 1000, 906, 88, 87, 86, 50, 13, 3 is wrong

# counts number of non-prime numbers
b = (79 *100) + 100000
c = b + 17000
z = 0
count = 0
for x in range(b, c+1, 17):
	count += 1
	for y in range(2, x):
		if (x % y) == 0:
			print("{} divides into {} {} times".format(y, x, float(x) / float(y)))
			z += 1
			break
print("z: ", z)
print("count: ", count)
b = 107900 
c = 109600 
h = 0
g = 1
# loop a
while g != 0:
	print(b, h)
	f = 1
	d = 2
	# loop b
	while (g != 0):
		e = 2
		# loop c
		while (g != 0):
			g = ((d * e) - b)
			if g == 0:
				f = 0 
			e += 1 
			g = (e - b)
		d += 1
		g = (d - b)
	if f == 0:
		h += 1 
	g = (b - c)
	b += 17
print(h)

'''
set b 79
set c b
jnz a 2
jnz 1 5
mul b 100
sub b -100000
set c b
sub c -17000
set f 1 	< LABEL A
set d 2
set e 2 	< LABEL B
set g d 	< LABEL C
mul g e
sub g b
jnz g 2
set f 0
sub e -1
set g e
sub g b
jnz g -8 	goto C
sub d -1
set g d
sub g b
jnz g -13 	goto B
jnz f 2
sub h -1
set g b
sub g c
jnz g 2
jnz 1 3
sub b -17 
jnz 1 -23 	goto A
'''