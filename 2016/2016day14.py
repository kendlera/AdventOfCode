# day 14 of advent of code
import threading
import hashlib
import re

START = "jlmsuwbz"
ITEMS = {}    		# we need a list of {index : character}
PATTERN3 = re.compile(r"(\w)\1{2,}")
PATTERN5 = re.compile(r"(\w)\1{4,}")
KEY_INDEXES = []

def generateText(seed):
	for x in range(2017):
		algorithm = hashlib.md5()
		algorithm.update(seed)
		seed = algorithm.hexdigest()
	return seed

def hasFive(text):
	result = PATTERN5.findall(text)
	return result

def hasThree(text):
	result = PATTERN3.findall(text)
	return result

def manageSearch():
	for index in range(50000):
		seed = START + str(index)
		key = generateText(seed)
		patterns3 = hasThree(key)
		old = []
		if len(patterns3) > 0:
			patterns5 = hasFive(key)
			for item in ITEMS:
				if item < (index - 1000): 	# out of scope
					old.append(item)
					continue
				#for found in patterns5:
				if ITEMS[item] in patterns5:
						# we found a key!
					KEY_INDEXES.append(item)
					old.append(item)
						#if len(KEY_INDEXES) == 64:
						#else:
					print "Found key", item
			ITEMS[index] = patterns3[0] # add to dictionary
		for i in old: 
			if i in ITEMS:
				del ITEMS[i] 
	print len(KEY_INDEXES)
	print sorted(KEY_INDEXES)
	print sorted(KEY_INDEXES)[63]

manageSearch()