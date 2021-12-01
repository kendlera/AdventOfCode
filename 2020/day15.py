def partOne():
    numbersSaid = 6
    numbers = {1: 1, 20: 2, 8: 3, 12: 4, 0: 5, 14: 6}
    lastNumberSaid = 14
    nextNumber = 0
    while numbersSaid < 30000001:
        numbersSaid += 1
        if numbersSaid == 30000000:
            print(nextNumber)
        if nextNumber in numbers:
            lastSaid = numbers[nextNumber]
            diff = numbersSaid - lastSaid 
            numbers[nextNumber] = numbersSaid
            nextNumber = diff 
        else:
            numbers[nextNumber] = numbersSaid
            nextNumber = 0
    # print(numbers)

partOne()
