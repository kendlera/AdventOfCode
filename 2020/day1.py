def parseInput():
    expenses = []
    with open('input.txt', 'r') as f:
        expenses = f.readlines()
    for i in range(len(expenses)):
        expenses[i] = int(expenses[i])
    return sorted(expenses)

def partOne():
    sorted_expenses = parseInput()
    print(sorted_expenses)
    for expense in sorted_expenses:
        if expense > 1010:
            print("did not find sum")
            return
        other_num = 2020 - expense 
        try:
            sorted_expenses.index(other_num)
        except ValueError:
            # not a match
            continue
        print("found a match!", expense, other_num)
        print(expense * other_num)
        return

def partTwo():
    sorted_expenses = parseInput()
    for expense_idx1 in range(len(sorted_expenses)):
        for expense_idx2 in range(expense_idx1+1, len(sorted_expenses)):
            target_num = (2020 - (sorted_expenses[expense_idx1] + sorted_expenses[expense_idx2]))
            if target_num < sorted_expenses[expense_idx2]:
                print("did not find sum")
                return
            try:
                sorted_expenses.index(target_num)
            except ValueError:
                # not a match
                continue
            print("found a match!", sorted_expenses[expense_idx1], sorted_expenses[expense_idx2], target_num)
            print(sorted_expenses[expense_idx1] * sorted_expenses[expense_idx2] * target_num)
            return

# partOne()
# partTwo()