def parse_data():
    with open("puzzle_input.txt", 'r') as f:
        lines = f.readlines()
    parsed_lines = []
    for line in lines:
        readings, output = line.strip().split(" | ")
        parsed_lines.append([readings.split(), output.split()])
    return parsed_lines 

def part_one():
    lines = parse_data()
    unique_lens = [2, 4, 3, 7]
    total_unique = 0
    for line in lines:
        reading, output = line
        for elem in output:
            if len(elem) in unique_lens:
                total_unique += 1

    print(total_unique)

def part_two():
    lines = parse_data()
    decoded = [0,0,0,0,0,0,0,0,0,0]
    total = 0
    for line in lines:
        reading, output = line 
        # sort by length
        sreading = sorted(reading, key=lambda x: len(x))
        # pick out unique length entries
        decoded[1] = "".join(sorted(sreading[0]))
        decoded[4] = "".join(sorted(sreading[2]))
        decoded[7] = "".join(sorted(sreading[1]))
        decoded[8] = "".join(sorted(sreading[9]))
        # decode length six entries
        six_candidates = sreading[6:9]
        for candidate in six_candidates:
            if not (decoded[1][0] in candidate and decoded[1][1] in candidate):
                # this is the number six!
                decoded[6] = "".join(sorted(candidate))
            elif (decoded[4][0] in candidate and decoded[4][1] in candidate and decoded[4][2] in candidate and decoded[4][3] in candidate):
                # this is the number nine!
                decoded[9] = "".join(sorted(candidate))
            else:
                # this is the number zero!
                decoded[0] = "".join(sorted(candidate)) 
        five_candidates = sreading[3:6]
        for candidate in five_candidates:
            if (decoded[1][0] in candidate and decoded[1][1] in candidate):
                # this is the number three!
                decoded[3] = "".join(sorted(candidate)) 
            elif (candidate[0] in decoded[6] and candidate[1] in decoded[6] and candidate[2] in decoded[6] and candidate[3] in decoded[6] and candidate[4] in decoded[6]):
                # this is number five!
                decoded[5] = "".join(sorted(candidate))
            else:
                # this is number two!
                decoded[2] = "".join(sorted(candidate))
        # now that we've decoded all the entries, create the output
        full_digit = ""
        for num in output:
            snum = "".join(sorted(num))
            try:
                digit = decoded.index(snum)
            except ValueError:
                return
            full_digit += str(digit) 
        total += int(full_digit)
    print(total)
