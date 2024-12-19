from collections import defaultdict
from functools import cache
f = open('aoc19.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
components = tuple(raw_input[0].split(', '))
towels = raw_input[2:]
TOWELS_MADE = defaultdict(int)
towels_made = 0
@cache
def can_make(components, towel):
    count = 0
    for component in components:
        if towel == '':
            return 1
        if towel.startswith(component):
            count += can_make(components, towel[len(component):])
    return count

for x, towel in enumerate(towels):
    result = can_make(components, towel) 
    if result > 0:
        towels_made += 1
        TOWELS_MADE[towel] = result
print('Part 1: you can make ' + str(towels_made) + ' towels')
print('Part 2: There are ' + str(sum(TOWELS_MADE.values())) + ' ways to make towels')

