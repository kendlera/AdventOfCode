
def read_perpendicular_lines():
    with open("puzzle_input.txt", 'r') as f:
        lines = f.readlines()
    parsed_horiz_lines = []
    parsed_vert_lines = []
    parsed_diag_lines = []
    for line in lines:
        coord1, coord2 = line.strip().split(" -> ")
        pos11, pos12 = coord1.split(",")
        pos21, pos22 = coord2.split(",")
        if pos11 == pos21:
            parsed_vert_lines.append([[int(pos11), int(pos12)], [int(pos21), int(pos22)]])
        elif pos12 == pos22:
            parsed_horiz_lines.append([[int(pos11), int(pos12)], [int(pos21), int(pos22)]])
        else:
            parsed_diag_lines.append([[int(pos11), int(pos12)], [int(pos21), int(pos22)]])
    return parsed_vert_lines, parsed_horiz_lines, parsed_diag_lines

def part_one_nosort():
    vert_lines, horiz_lines, diag_lines = read_perpendicular_lines()
    point_counts = {}
    for line in vert_lines:
        # print(line)
        start = min([line[0][1], line[1][1]])
        stop = max([line[0][1], line[1][1]])
        x = line[0][0]
        for y in range(start, stop+1):
            if x not in point_counts:
                point_counts[x] = {}
                point_counts[x][y] = 1 
            elif y not in point_counts[x]:
                point_counts[x][y] = 1 
            else:
                point_counts[x][y] += 1 
    for line in horiz_lines:
        # print(line)
        start = min([line[0][0], line[1][0]])
        stop = max([line[0][0], line[1][0]])
        y = line[0][1]
        for x in range(start, stop+1):
            if x not in point_counts:
                point_counts[x] = {}
                point_counts[x][y] = 1 
            elif y not in point_counts[x]:
                point_counts[x][y] = 1 
            else:
                point_counts[x][y] += 1 
    for line in diag_lines:
        if line[0][0] < line[1][0]:
            startx = line[0][0]
            stopx = line[1][0]
            y = line[0][1]
            if line[0][1] < line[1][1]:
                slope = 1 
            else:
                slope = -1 
        else:
            startx = line[1][0]
            stopx = line[0][0]
            y = line[1][1]
            if line[1][1] < line[0][1]:
                slope = 1 
            else:
                slope = -1 
        for x in range(startx, stopx+1):
            if x not in point_counts:
                point_counts[x] = {}
                point_counts[x][y] = 1 
            elif y not in point_counts[x]:
                point_counts[x][y] = 1 
            else:
                point_counts[x][y] += 1 
            y += slope

    total = 0 
    for x in point_counts:
        for y in point_counts[x]:
            if point_counts.get(x).get(y) > 1:
                total += 1 
    print(total)

part_one_nosort()
