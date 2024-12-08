f = open('aoc08.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
antinode_locations = set()
rows = len(raw_input)
cols = len(raw_input[0])
antenna_info = {}

def signed_distance(p1, p2):
    p1_x = p1[0]
    p1_y = p1[1]
    p2_x = p2[0]
    p2_y = p2[1]
    x_distance = p2_x - p1_x
    y_distance = p2_y - p1_y
    return(x_distance, y_distance)

for row, line in enumerate(raw_input):
    for col, item in enumerate(line):
        if item != '.':
            if item not in antenna_info:
                antenna_info[item] = []
            antenna_info[item] += [(row, col)]

# Determine where the antinodes are
for antenna in antenna_info:
    a_locs = antenna_info[antenna][:]
    for x in range(len(a_locs) - 1):
        current_loc = a_locs.pop(0)
        for next_loc in a_locs:
            distance = signed_distance(current_loc, next_loc)
            anti_loc = (current_loc[0] - distance[0], current_loc[1] - distance[1])
            if not (anti_loc[0] < 0 or anti_loc[0] >= rows or anti_loc[1] < 0 or anti_loc[1] >= cols):
                antinode_locations.add(anti_loc)
            anti_loc = (next_loc[0] + distance[0], next_loc[1] + distance[1])
            if not (anti_loc[0] < 0 or anti_loc[0] >= rows or anti_loc[1] < 0 or anti_loc[1] >= cols):
                antinode_locations.add(anti_loc)
print('Part 1: there are ' + str(len(list(antinode_locations))) + ' unique antinode locations.')

# Part 2, clear out the set of antinodes
antinode_locations = set()
for antenna in antenna_info:
    a_locs = antenna_info[antenna][:]
    for x in range(len(a_locs) - 1):
        current_loc = a_locs.pop(0)
        for next_loc in a_locs:
            distance = signed_distance(current_loc, next_loc)
            # Go from start antenna forwards
            next_x = current_loc[0] + distance[0]
            next_y = current_loc[1] + distance[1]
            while (next_x >= 0 and next_x < rows and next_y >= 0 and next_y < cols):
                antinode_locations.add((next_x, next_y))
                next_x += distance[0]
                next_y += distance[1]
            # go from distant antenna backards
            next_x = next_loc[0] - distance[0]
            next_y = next_loc[1] - distance[1]
            while (next_x >= 0 and next_x < rows and next_y >= 0 and next_y < cols):
                antinode_locations.add((next_x, next_y))
                next_x -= distance[0]
                next_y -= distance[1]
print('Part 2: there are ' + str(len(list(antinode_locations))) + ' unique antinode locations.')
