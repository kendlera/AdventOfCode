
class Octopus:
    def __init__(self, x, y, energy_level):
        self.x = x 
        self.y = y
        self.energy_level = energy_level
        self.neighbors = []
        self.did_flash = False

    def step(self):
        self.energy_level += 1

    def does_flash(self):
        if not self.did_flash and self.energy_level > 9:
            # we flash!
            self.did_flash = True
            self.energy_level = 0
            for n in self.neighbors:
                n.step() 
                n.does_flash()

    def reset(self):
        if self.did_flash:
            self.energy_level = 0
        temp = self.did_flash
        self.did_flash = False
        return temp

def read_input():
    with open("puzzle_input.txt", 'r') as f:
        lines = f.readlines()
    return lines

def construct_octopuses():
    lines = read_input()
    mapping = {}
    # construct octopuses
    for r in range(len(lines)):
        for c in range(len(lines[0].strip())):
            octo = Octopus(r, c, int(lines[r][c]))
            mapping["%d%d" % (r, c)] = octo 

    # link neighbors
    for r in range(len(lines)):
        for c in range(len(lines[0].strip())):
            current = mapping.get("%d%d" % (r, c))
            if r > 0:
                if c > 0:
                    # top left
                    current.neighbors.append(mapping.get("%d%d" % (r-1, c-1)))
                # top
                current.neighbors.append(mapping.get("%d%d" % (r-1, c)))
                if c < (len(lines[0].strip())-1):
                    # top right
                    current.neighbors.append(mapping.get("%d%d" % (r-1, c+1)))
            if c > 0:
                # left
                current.neighbors.append(mapping.get("%d%d" % (r, c-1)))
            if c < (len(lines[0].strip())-1):
                # right
                current.neighbors.append(mapping.get("%d%d" % (r, c+1)))
            if r < (len(lines) - 1):
                if c > 0:
                    # bottom left
                    current.neighbors.append(mapping.get("%d%d" % (r+1, c-1)))
                # bottom
                current.neighbors.append(mapping.get("%d%d" % (r+1, c)))
                if c < (len(lines[0].strip())-1):
                    # bottom right
                    current.neighbors.append(mapping.get("%d%d" % (r+1, c+1)))
    return mapping

def step_octopuses():
    octopuses = construct_octopuses()
    num_octopuses = len(octopuses)
    for s in range(1000):
        total_flashes = 0
        for o in octopuses:
            octopuses.get(o).step()
        for o in octopuses:
            octopuses.get(o).does_flash()
        for o in octopuses:
            did_flash = octopuses.get(o).reset()
            # print(octopuses.get(o).x, octopuses.get(o).y, octopuses.get(o).energy_level)
            if did_flash:
                total_flashes += 1
        if total_flashes == num_octopuses:
            print(s)
            return
