from collections import defaultdict
import math

f = open('aoc14.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()

rows = 103
cols = 101
grid = []
for row in range(rows):
    current_row = [0] * cols
    grid += [current_row]
robot_map = defaultdict(int)

cycles = 100
for line in raw_input:
    
    pos_raw, vel_raw = line.split(' ')
    pos = [int(x) for x in pos_raw.split('=')[1].split(',')]
    vel = [int(x) for x in vel_raw.split('=')[1].split(',')]
    # Get x
    new_x = (pos[0] + cycles * vel[0]) % cols
    new_y = (pos[1] + cycles * vel[1]) % rows
    robot_map[(new_x, new_y)] += 1
    
def get_safety_factor(robot_map, rows, cols):
# find robots in each quadrant
    half_width = cols // 2
    half_height = rows // 2
    # quadrant 1
    robots = [x for x in robot_map if x[0] < half_width and x[1] < half_height]
    q1 = 0
    for robot in robots:
        q1 += robot_map[robot]
    # quadrant 2
    robots = [x for x in robot_map if x[0] > half_width and x[1] < half_height]
    q2 = 0
    for robot in robots:
        q2 += robot_map[robot]
    # q3
    q3 = 0
    robots = [x for x in robot_map if x[0] > half_width and x[1] > half_height]
    for robot in robots:
        q3 += robot_map[robot]
    # q4
    q4 = 0
    robots = [x for x in robot_map if x[0] < half_width and x[1] > half_height]
    for robot in robots:
        q4 += robot_map[robot]
    safety_factor = q1 * q2 * q3 * q4
    return safety_factor
part1_safety_factor = get_safety_factor(robot_map, rows, cols)
# Part 2
final_cycle = 0

for cycle in range(10000):
    robot_map = defaultdict(int)
    for line in raw_input:
        pos_raw, vel_raw = line.split(' ')
        pos = [int(x) for x in pos_raw.split('=')[1].split(',')]
        vel = [int(x) for x in vel_raw.split('=')[1].split(',')]
        # Get x
        new_x = (pos[0] + cycle * vel[0]) % cols
        new_y = (pos[1] + cycle * vel[1]) % rows
        robot_map[(new_x, new_y)] += 1
   # See if one of the robots are overlapping, assuming the tree happens when nothing overlaps
    overlapping = [x for x in robot_map.values() if x > 1]
    if len(overlapping) == 0:
        # Nothing overlapping
        final_cycle = cycle
        break

print('Part 1: safety factor is ' + str(part1_safety_factor))
print('Part 2: it takes ' + str(final_cycle) + ' cycles to make a christmas tree')

