import re

f = open('aoc03.txt','rt')
raw_input = []
for line in f:
    raw_input += [line.strip()]
f.close()
mul_results = []

mul_value = 0 
for line in raw_input:
    mul_results += re.findall("mul[(][0-9]{1,3},[0-9]{1,3}[)]", line)
mul_value = 0
for result in mul_results:
    numbers = [int(x) for x in result[4:-1].split(",")]
    mul_value += numbers[0] * numbers[1]
print('Part 1: sum of all multiplication instructions is ' + str(mul_value))

# ************* Part 2

mul_value = 0
enabled = True
for line in raw_input:
    mul_results = []
    mul_indices = []
    if enabled:
        do_indices = [-1] # Start enabled
        dont_indices = [-2] # Really start disabled then later switch to enabled
    else:
        do_indices = [-2]
        dont_indices = [-1]
    mul_results += re.findall("mul[(][0-9]{1,3},[0-9]{1,3}[)]", line)
    mul_indices += [x.start(0) for x in re.finditer("mul[(][0-9]{1,3},[0-9]{1,3}[)]", line)]
    do_indices += [x.start(0) for x in re.finditer("do[(][)]", line)]
    dont_indices += [x.start(0) for x in re.finditer("don't[(][)]", line)]


    for i, result in enumerate(mul_results):
        index = mul_indices[i]
    
        
        earlier_dont = [x for x in dont_indices if x < index]
        earlier_do = [x for x in do_indices if x < index]
        if earlier_dont[-1] > earlier_do[-1]:
            enabled = False
        else:
            enabled = True
        # Check for multiple do()
        if enabled:
            numbers = [int(x) for x in result[4:-1].split(",")]
            mul_value += numbers[0] * numbers[1]
print('Part 2: sum of all multiplication instructions with do/dont activated is ' + str(mul_value))
# 74956953 too low