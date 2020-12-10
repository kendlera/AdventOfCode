def parseInput():
    with open('input.txt', 'r') as f:
        nums = f.readlines()
    parsedNums = []
    for n in nums:
        parsedNums.append(int(n))
    return parsedNums 

def partOne():
    nums = parseInput()
    for idx in range(25, len(nums)):
        curr = nums[idx]
        options = nums[idx - 25:idx]
        found = False
        for op in options:
            reciprocal = curr - op
            if reciprocal > 0 and reciprocal != op and reciprocal in options:
                found = True
                break
        if not found:
            print(curr)
            return
    # 22477624

def partTwo():
    nums = parseInput()
    targetSum = 22477624
    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            total += nums[j]
            if (total == targetSum):
                rangeInts = nums[i:j+1]
                minInt = min(rangeInts)
                maxInt = max(rangeInts)
                print(minInt, maxInt, minInt + maxInt)
                return 
            elif (total > targetSum):
                continue
