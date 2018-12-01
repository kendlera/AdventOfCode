connectors = "48/5 25/10 35/49 34/41 35/35 47/35 34/46 47/23 28/8 27/21 40/11 22/50 48/42 38/17 50/33 13/13 22/33 17/29 "
connectors += "50/0 20/47 28/0 42/4 46/22 19/35 17/22 33/37 47/7 35/20 8/36 24/34 6/7 7/43 45/37 21/31 37/26 16/5 11/14 7/23 "
connectors += "2/23 3/25 20/20 18/20 19/34 25/46 41/24 0/33 3/7 49/38 47/22 44/15 24/21 10/35 6/21 14/50"

'''
Approach: for each component with a 0 port, create a tree. whichever tree has the "heaviest" branch wins with that branch as the bridge.
'''

class Component:
	def __init__(self, parent, pins):
		self.parent = parent 
		self.ident = str(pins)
		self.children = []
		self.pins = pins

	def has_ancestor(self, other_pins):
		target = str(other_pins)
		ancestor = self.parent
		while ancestor is not None:
			if ancestor.ident == target:
				return True 
			ancestor = ancestor.parent
		return False

	def get_depth(self):
		count = 1
		ancestor = self.parent
		while ancestor is not None:
			count += 1 
			ancestor = ancestor.parent
		return count

	def print_stats(self):
		ancestor = self.parent 
		count = 1 
		total = sum(self.pins) 
		while ancestor is not None:
			count += 1 
			total += sum(ancestor.pins) 
			ancestor = ancestor.parent
		# print("Branch ending in {} has length {} and weight {}".format(self.ident, count, total))
		return [count, total]

def parse_components(text):
	elems = text.split(' ') 
	components = [] 
	for elem in elems:
		pins1, pins2 = elem.split('/')
		components.append([int(pins1), int(pins2)])
	return components

def build_tree(component, open_pin, connectors):
	num_components = len(connectors)
	# print("Progress: depth {} out of {} connectors".format(component.get_depth(), num_components))
	for idx in range(num_components):
		if (open_pin in connectors[idx]) and (str(connectors[idx]) != component.ident) and (not component.has_ancestor(connectors[idx])):
			obj = Component(component, connectors[idx])
			component.children.append(obj) 
	if len(component.children) == 0:
		# no compatible connectors! we're at a leaf node. 
		weight = component.print_stats()
		return weight
	else:
		weights = []
		for child in component.children: 
			if child.pins[0] == open_pin:
				weights.append(build_tree(child, child.pins[1], connectors))
			else:
				weights.append(build_tree(child, child.pins[0], connectors))
		# print(weights)
		longest = max(weights, key=lambda x: x[0])[0]
		ties = [x for x in weights if x[0] == longest]
		winner = max(ties, key=lambda x: x[1])
		return winner

def operator():
	components = parse_components(connectors)
	roots = [] 
	for component in components:
		if 0 in component:
			obj = Component(None, component)
			roots.append(obj) 
	winners = []
	for root in roots:
		if root.pins[0] == 0:
			branches = build_tree(root, root.pins[1], components)
		else:
			branches = build_tree(root, root.pins[0], components)
		print(branches)
		# strongest = max(branches)
		# winners.append(strongest)
		print("Maximum branch with root {} is length {} with strength{}".format(root.ident, branches[0], branches[1]))
	print("Done!", winners)


def check_duplicates():
	elems = connectors.split() 
	for elem in range(len(elems)):
		if elems[elem] in elems[elem+1:]:
			print("Duplicate!", elems[elem])
	print('done')
# check_duplicates()
# operator()
