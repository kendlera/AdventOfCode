def parse_pairs():
    with open("puzzle_input.txt", 'r') as f:
        lines = f.readlines()
    parsed = []
    for line in lines:
        elems = line.strip().split("-")
        parsed.append(elems)
    return parsed 

def get_children(pairs, root, path):
    children = []
    for pair in pairs:
        if root in pair:
            other_idx = (1 - pair.index(root))
            other = pair[other_idx]
            if other.isupper() or other not in path:
                children.append(pair[other_idx])
    return children

def traverse_tree(tree, path, pairs):
    for root in tree:
        if root == "end":
            continue
        children = list(tree.get(root).keys())
        if len(children) == 0:
            # this is a leaf!
            children = get_children(pairs, root, path)
            for child in children:
                tree[root][child] = {} 
        traverse_tree(tree[root], path + "," + root, pairs)

def count_roots(tree):
    total = 0
    for root in tree:
        if root == "end":
            total += 1
            continue
        total += count_roots(tree[root])
    return total

def part_one():
    pairs = parse_pairs()
    tree = {'start': {}}
    traverse_tree(tree, "", pairs)
    print(count_roots(tree))
# ------------------------------------------------------------

class Node:
    def __init__(self, val):
        self.visited = 0
        self.value = val
        self.neighbors = []

    def can_visit(self, path):
        if self.value == "start":
            return False, ""
        if self.value.isupper() or self.value == "end":
            return True, ""
        if self.value not in path:
            return True, ""
        if "*" in path:
            return False, ""
        # if there is no * value, and the value is in the path, we can visit one more time
        return True, "*"


def traverse_nodes(current, path):
    current.visited += 1
    if current.value == "end":
        # do not visit neighbors
        return
    appended_path = path + "," + current.value
    for n in current.neighbors:
        visitable, path_char = n.can_visit(appended_path)
        if visitable:
            traverse_nodes(n, path_char + appended_path)

def part_two():
    nodes = {}
    pairs = parse_pairs()
    for pair in pairs:
        first, second = pair 
        # create if necessary
        if first not in nodes:
            nodes[first] = Node(first)
        if second not in nodes:
            nodes[second] = Node(second)
        # link neighbors
        nodes[first].neighbors.append(nodes[second])
        nodes[second].neighbors.append(nodes[first])
    print("tree constructed")
    traverse_nodes(nodes["start"], "")
    print(nodes["end"].visited)
