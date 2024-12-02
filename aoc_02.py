import math
f = open('aoc02.txt','rt')
raw_input = []
for line in f:
    raw_input += [line.strip()]
f.close()

def safe(line):
    inc = True
    dec = True
    for x, num in enumerate(line[1:]):
        if line[x + 1] - line[x] < 1 or line[x + 1] - line[x] > 3:
            inc = False
        if line[x + 1] - line[x] > -1 or line[x + 1] - line[x] < -3:
            dec = False
    return inc or dec

def part2_safe(line):
    # Going to iterate and remove one number at a time.  The first safe hit means it can be modified
    # Otherwise it can't be made safe
    # NOTE: reports which are always safe will also pass this

    for x in range(len(line)):
        new_line = line[:x] + line[x+1:]
        if safe(new_line):
            return True
    return False

safe_reports = 0
for line in raw_input:
    report = [int(x) for x in line.split()]
    
    if safe(report):
        safe_reports += 1
print('Part 1: there are ' + str(safe_reports) + ' safe reports.')

safe_reports = 0

for line in raw_input:
    report = [int(x) for x in line.split()]
    
    if part2_safe(report):
        safe_reports += 1
print('Part 2: there are ' + str(safe_reports) + ' safe reports.')
# 438 too low
# 439 too low
# 444 too low

