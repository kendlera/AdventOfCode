def parseInput():
    with open('input.txt', 'r') as f:
        rules = f.readlines()
    # { leaf : [parents]}
    parsed = {}
    for rule in rules:
        container, contained = rule.strip().split(' contain ')
        container = container.replace(' bags', '')
        for bag in contained.split(', '):
            cleaned = bag.replace(' bags', '').replace(' bag', '').replace('.', '')
            cleaned = cleaned[2:]
            if cleaned in parsed:
                parsed[cleaned].append(container)
            else:
                parsed[cleaned] = [container]
    return parsed


def partOne():
    bagTree = parseInput()
    targetBag = 'shiny gold'
    containers = bagTree[targetBag]
    total = len(containers)
    queue = containers
    seen = containers[:]
    while len(queue) != 0:
        # assumes no loops
        curr = queue[0]
        queue = queue[1:]
        if curr in bagTree:
            containers = bagTree[curr]
            for bag in containers:
                if bag not in seen:
                    total += 1
                    queue.append(bag)
                    seen.append(bag)
        else:
            # this is a top-most bag
            pass
    print(total)

# partOne()


def parsedTwo():
    with open('input.txt', 'r') as f:
        rules = f.readlines()
    # { parent : [[leaf, count], ....]}
    parsed = {}
    for rule in rules:
        container, contained = rule.strip().split(' contain ')
        container = container.replace(' bags', '')
        for bag in contained.split(', '):
            cleaned = bag.replace(' bags', '').replace(' bag', '').replace('.', '')
            if cleaned[0] == 'n':
                # leaf node
                continue
            numBags = int(cleaned[0])
            cleaned = cleaned[2:]
            if container in parsed:
                parsed[container].append([cleaned, numBags])
            else:
                parsed[container] = [[cleaned, numBags]]
    return parsed

def partTwo():
    bagTree = parsedTwo()
    rootBag = 'shiny gold'
    print(countBagsRecursion(bagTree, rootBag))

def countBagsRecursion(bagTree, root):
    if root not in bagTree:
        # leaf node
        return 1
    numBags = 1 # itself 
    for elem in bagTree[root]:
        bag, numContained = elem
        bagHolds = countBagsRecursion(bagTree, bag)
        numBags += (bagHolds * numContained)
    return numBags 
