from copy import deepcopy
f = open('aoc06.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
guard_positions = set()
# Find the starting position
for row, line in enumerate(raw_input):
    raw_input[row] = [x for x in line]
    for col, position in enumerate(line):
        if position == '^':
            guard_pos = (row, col)
original_map = deepcopy(raw_input)
original_guard_pos = deepcopy(guard_pos)
rows = len(raw_input)
cols = len(raw_input[0])
# Time to loop!
direction = (-1,0)
while True:
    guard_positions.add(guard_pos)
    row = guard_pos[0]
    col = guard_pos[1]
    next_row = row + direction[0]
    next_col = col + direction[1]
    # Determine if out of top or bottom
    if next_row == -1 or next_row == rows:
        break
    # determine if out of left or right
    if next_col == -1 or next_col == cols:
        break
    next_pos = raw_input[next_row][next_col]
    if next_pos != '#':
        # we can move there.  So move.
        raw_input[row][col] = '.'
        raw_input[next_row][next_col] = '^'
        guard_pos = (next_row, next_col)
    else:
        # Just change direction, we will update position in the next loop
        direction = (direction[1], -1 * direction[0])
positions_visited = len(list(guard_positions))
print('Part 1: the guard visited ' + str(positions_visited) + ' positions.')

loop_obstructions = 0
for parent_row in range(rows):
    for parent_col in range(cols):
        raw_input = deepcopy(original_map)
        if raw_input[parent_row][parent_col] == '.':
            raw_input[parent_row][parent_col] = '#'
        else:
            continue
        guard_pos = deepcopy(original_guard_pos)
        direction = (-1,0)
        my_counter = 0
        for counter in range(20000):
            my_counter += 1
            row = guard_pos[0]
            col = guard_pos[1]
            next_row = row + direction[0]
            next_col = col + direction[1]
            # Determine if out of top or bottom
            if next_row == -1 or next_row == rows:
                break
            # determine if out of left or right
            if next_col == -1 or next_col == cols:
                break
            next_pos = raw_input[next_row][next_col]
            if next_pos != '#':
                # we can move there.  So move.
                raw_input[row][col] = '.'
                raw_input[next_row][next_col] = '^'
                guard_pos = (next_row, next_col)
            else:
                # Just change direction, we will update position in the next loop
                direction = (direction[1], -1 * direction[0])
        if my_counter == 20000:
            loop_obstructions += 1
print('Part 2: there are ' + str(loop_obstructions) + ' places where we can create a guard loop')