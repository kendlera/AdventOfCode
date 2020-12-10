def parseInstructions():
    with open('input.txt', 'r') as f:
        instructions = f.readlines()
    data = []
    for inst in instructions:
        i, val = inst.strip().split(' ')
        data.append([i, int(val)])
    return data

def partOne(instructions):
    idx = 0
    accumulator = 0
    done = False
    seen = []
    while not done:
        if idx in seen or idx == len(instructions):
            break
        seen.append(idx)
        op, val = instructions[idx]
        if (op == 'nop'):
            idx += 1
        elif (op == 'acc'):
            accumulator += val
            idx += 1
        elif (op == 'jmp'):
            idx += val
        else:
            print("Unknown operation", op)
    print(accumulator)
    return idx, accumulator

# partOne()
def partTwo():
    instructions = parseInstructions()
    target = len(instructions)
    for i in range(len(instructions)):
        op, val = instructions[i]
        if op == 'nop':
            tempInst = instructions[:i] + [['jmp', val]] + instructions[i+1:]
            idx, acc = partOne(tempInst)
            if (idx == target): 
                print(acc)
                return
        elif op == 'jmp':
            tempInst = instructions[:i] + [['nop', val]] + instructions[i+1:]
            idx, acc = partOne(tempInst)
            if (idx == target): 
                print(acc)
                return

partTwo()
