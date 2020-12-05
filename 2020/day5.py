def parseInput():
    with open('input.txt', 'r') as f:
        seats = f.readlines()
    parsed = []
    for seat in seats:
        row = seat[:7]
        row = row.replace('F', '0')
        row = row.replace('B', '1')
        parsedRow = int(row, 2)
        col = seat[7:]
        col = col.replace('R', '1')
        col = col.replace('L', '0')
        parsedCol = int(col, 2)
        parsed.append([parsedRow, parsedCol])
    return parsed 


def partOne():
    seats = parseInput()
    maxScore = 0
    for seat in seats:
        row, col = seat 
        score = (row * 8) + col 
        maxScore = max(score, maxScore)
    print(maxScore)


def partTwo():
    seats = parseInput()
    seatScore = []
    for seat in seats:
        row, col = seat 
        score = (row * 8) + col 
        seatScore.append(score)
    sortedScores = sorted(seatScore)
    lastScore = sortedScores[0] - 1
    for score in sortedScores:
        if score != (lastScore + 1):
            print(score)
        lastScore = score
