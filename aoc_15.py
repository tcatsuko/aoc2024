f = open('aoc15.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
# Split off the map from the instructions
room_map = []
instruction_start = 0
for line_num, line in enumerate(raw_input):
    if line == '':
        instruction_start = line_num + 1
        break
    room_map += [[x for x in line]]
instructions = []
for line in raw_input[instruction_start:]:
    instructions += [x for x in line]
# Find the starting position
for row, line in enumerate(room_map):
    for col, item in enumerate(line):
        if item == '@':
            start_pos = (row, col)
# Start to go through the instructions
robot = start_pos
while instructions:
    ####################
    # Y IS ROW
    # X IS COL
    # ROBOT IS STORED (Y,X)
    next_instruction = instructions.pop(0)
    if next_instruction == '<':
        # left
        dx = -1
        dy = 0
    elif next_instruction == '>':
        # right
        dx = 1
        dy = 0
    elif next_instruction == '^':
        # up
        dx = 0
        dy = -1
    elif next_instruction == 'v':
        dx = 0
        dy = 1
    current_y = robot[0]
    current_x = robot[1]
    next_y = current_y + dy
    next_x = current_x + dx
    can_move = False
    has_rock = False
    next_item = room_map[next_y][next_x]
    while next_item != "#":
        if next_item == '.':
            can_move = True
            break
        if next_item == 'O':
            has_rock = True
        next_y += dy
        next_x += dx
        next_item = room_map[next_y][next_x]
    if can_move:
        room_map[current_y][current_x] = '.'
        room_map[current_y + dy][current_x + dx] = '@'
        if has_rock:
            room_map[next_y][next_x] = 'O'
        robot = (current_y + dy, current_x + dx)

# get GPS coordinates of each box
gps_sum = 0
for row, line in enumerate(room_map):
    for col, item in enumerate(line):
        if item == 'O':
            gps_sum += (100 * row + col)
print('Part 1: sum of GPS coordinates is ' + str(gps_sum))

# Part 2
# Redraw the room map

def can_move_vert(room_map, lcol, rcol, start_row, dy):
    # check left col
    l_move = False
    r_move = False
    next_row = start_row + dy
    next_item = room_map[next_row][lcol]
    while next_item != '#':
        if next_item == ']':
            # New right column, check if that one can move
            left_check = can_move_vert(room_map, lcol - 1, lcol, next_row, dy)
            if left_check == False:
                return False
        elif next_item == '.':
            l_move = True
            break
        next_row += dy
        next_item = room_map[next_row][lcol]
    
    # Check right column
    next_row = start_row + dy
    next_item = room_map[next_row][rcol]
    while next_item != '#':
        if next_item == '[':
            # New left column, check if that one can move
            right_check = can_move_vert(room_map, rcol, rcol + 1,next_row, dy)
            if right_check == False:
                return False
        elif next_item == '.':
            r_move = True
            break
        next_row += dy
        next_item = room_map[next_row][rcol]
    return l_move and r_move

def move_vert_one(room_map, start_row, lcol, dy):
    next_row = start_row + dy
    next_left = room_map[next_row][lcol]
    next_right = room_map[next_row][lcol + 1]
    
    if next_left == '[':
        move_vert_one(room_map, start_row + dy, lcol, dy)
    elif next_left == ']':
        move_vert_one(room_map, start_row + dy, lcol - 1, dy)
    if next_right == '[':
        move_vert_one(room_map, start_row + dy, lcol + 1, dy)
    room_map[next_row][lcol] = room_map[start_row][lcol]
    room_map[next_row][lcol + 1] = room_map[start_row][lcol + 1]
    room_map[start_row][lcol] = '.'
    room_map[start_row][lcol + 1] = '.'


    

room_map = []
for line in raw_input[:instruction_start - 1]:
    current_row = []
    for item in line:
        if item == '#':
            current_row += '#'
            current_row += '#'
        elif item == '.':
            current_row += '.'
            current_row += '.'
        elif item == 'O':
            current_row += '['
            current_row += ']'
        elif item == '@':
            current_row += '@'
            current_row += '.'
    room_map += [current_row]

instructions = []
for line in raw_input[instruction_start:]:
    instructions += [x for x in line]
# Find the starting position
for row, line in enumerate(room_map):
    for col, item in enumerate(line):
        if item == '@':
            start_pos = (row, col)
# Start to go through the instructions
robot = start_pos
while instructions:
    ####################
    # Y IS ROW
    # X IS COL
    # ROBOT IS STORED (Y,X)
    next_instruction = instructions.pop(0)
    if next_instruction == '<':
        # left
        dx = -1
        dy = 0
    elif next_instruction == '>':
        # right
        dx = 1
        dy = 0
    elif next_instruction == '^':
        # up
        dx = 0
        dy = -1
    elif next_instruction == 'v':
        dx = 0
        dy = 1
    current_y = robot[0]
    current_x = robot[1]
    next_y = current_y + dy
    next_x = current_x + dx
    
    next_item = room_map[next_y][next_x]
    if dx != 0:
        # left/right is way easier, start there
        can_move = False
        has_rock = False
        
        while next_item != "#":
            if next_item == '.':
                can_move = True
                open_space = (next_y, next_x)
                break
            if next_item == '[' or next_item == ']':
                has_rock = True
            next_y += dy
            next_x += dx
            next_item = room_map[next_y][next_x]
        if can_move:
            if has_rock:
                if dx == -1:
                    current_row = robot[0]
                    for x in range(next_x, robot[1]):
                        room_map[current_row][x] = room_map[current_row][x+1]
                    room_map[current_row][robot[1] - 1] = '@'
                    room_map[current_row][robot[1]] = '.'
                else:
                    current_row = robot[0]
                    for x in range(next_x, robot[1], -1):
                        room_map[current_row][x] = room_map[current_row][x-1]
                    room_map[current_row][robot[1]] = '.'
                    room_map[current_row][robot[1] + 1] = '@'
            else:
                room_map[current_y][current_x] = '.'
                room_map[current_y + dy][current_x + dx] = '@'
            robot = (current_y + dy, current_x + dx)
    elif dy != 0:
        next_item = room_map[robot[0] + dy][robot[1]]
        if next_item == '#':
            continue
        elif next_item == '.':
            # can move 
            room_map[robot[0] + dy][robot[1]] = '@'
            room_map[robot[0]][robot[1]] = '.'
            robot = (robot[0] + dy, robot[1])
        elif next_item == '[':
            can_move = can_move_vert(room_map, robot[1], robot[1] + 1, robot[0] + dy, dy)
            if can_move:
                move_vert_one(room_map, robot[0] + dy, robot[1], dy)
                room_map[robot[0] +dy ][robot[1]] = '@'
                room_map[robot[0]][robot[1]] = '.'
                robot = (robot[0] + dy, robot[1])
        elif next_item == ']':
            can_move = can_move_vert(room_map, robot[1] - 1, robot[1], robot[0] + dy, dy)
            if can_move:
                move_vert_one(room_map, robot[0] + dy, robot[1] - 1, dy)
                room_map[robot[0] + dy][robot[1]] = '@'
                room_map[robot[0]][robot[1]] = '.'
                robot = (robot[0] + dy, robot[1])
gps_sum = 0
for row, line in enumerate(room_map):
    for col, item in enumerate(line):
        if item == '[':
            gps_sum += (100 * row + col)
print('Part 2: GPS sum is ' + str(gps_sum))