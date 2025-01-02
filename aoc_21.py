from functools import cache
from collections import defaultdict

numeric_pad = {}
arrow_pad = {}
numeric_pad['A'] = {
    'A': 'A',
    '0': '<A',
    '1': '^<<A',
    '2': '<^A',
    '3': '^A',
    '4': '^^<<A',
    '5': '<^^A',
    '6': '^^A',
    '7': '^^^<<A',
    '8': '<^^^A',
    '9': '^^^A'
}
numeric_pad['0'] = {
     'A': '>A',
     '0': 'A',
     '1': '^<A',
     '2': '^A',
     '3': '^>A',
     '4': '^^<A',
     '5': '^^A',
     '6': '^^>A',
     '7': '^^^<A',
     '8': '^^^A',
     '9': '^^^>A'
}
numeric_pad['1'] = {
     'A': '>>vA',
     '0': '>vA',
     '1': 'A',
     '2': '>A',
     '3': '>>A',
     '4': '^A',
     '5': '^>A',
     '6': '^>>A',
     '7': '^^A',
     '8': '^^>A',
     '9': '^^>>A'
}
numeric_pad['2'] = {
     'A': 'v>A',
     '0': 'vA',
     '1': '<A',
     '2': 'A',
     '3': '>A',
     '4': '<^A',
     '5': '^A',
     '6': '^>A',
     '7': '<^^A',
     '8': '^^A',
     '9': '^^>A'
}
numeric_pad['3'] = {
     'A': 'vA',
     '0': '<vA',
     '1': '<<A',
     '2': '<A',
     '3': 'A',
     '4': '<<^A',
     '5': '<^A',
     '6': '^A',
     '7': '<<^^A',
     '8': '<^^A',
     '9': '^^A'
}
numeric_pad['4'] = {
     'A': '>>vvA',
     '0': '>vvA',
     '1': 'vA',
     '2': 'v>A',
     '3': 'v>>A',
     '4': 'A',
     '5': '>A',
     '6': '>>A',
     '7': '^A',
     '8': '^>A',
     '9': '^>>A'
}
numeric_pad['5'] = {
     'A': 'vv>A',
     '0': 'vvA',
     '1': '<vA',
     '2': 'vA',
     '3': 'v>A',
     '4': '<A',
     '5': 'A',
     '6': '>A',
     '7': '<^A',
     '8': '^A',
     '9': '^>A'
}
numeric_pad['6'] = {
     'A': 'vvA',
     '0': '<vvA',
     '1': '<<vA',
     '2': '<vA',
     '3': 'vA',
     '4': '<<A',
     '5': '<A',
     '6': 'A',
     '7': '<<^A',
     '8': '<^A',
     '9': '^A'
}
numeric_pad['7']= {
     'A': '>>vvvA',
     '0': '>vvvA',
     '1': 'vvA',
     '2': 'vv>A',
     '3': 'vv>>A',
     '4': 'vA',
     '5': 'v>A',
     '6': 'v>>A',
     '7': 'A',
     '8': '>A',
     '9': '>>A'
}
numeric_pad['8'] = {
     'A': 'vvv>A',
     '0': 'vvvA',
     '1': '<vvA',
     '2': 'vvA',
     '3': 'vv>A',
     '4': '<vA',
     '5': 'vA',
     '6': 'v>A',
     '7': '<A',
     '8': 'A',
     '9': '>A'
}
numeric_pad['9'] = {
     'A': 'vvvA',
     '0': '<vvvA',
     '1': '<<vvA',
     '2': '<vvA',
     '3': 'vvA',
     '4': '<<vA',
     '5': '<vA',
     '6': 'vA',
     '7': '<<A',
     '8': '<A',
     '9': 'A'
}
arrow_pad['A'] = {
     'A': 'A',
     '^': '<A',
     '<': 'v<<A',
     'v': '<vA',
     '>': 'vA'
}
arrow_pad['^'] = {
     'A': '>A',
     '^': 'A',
     '<': 'v<A',
     'v': 'vA',
     '>': 'v>A'
}
arrow_pad['<'] = {
     'A': '>>^A',
     '^': '>^A',
     '<': 'A',
     'v': '>A',
     '>': '>>A'
}
arrow_pad['v'] = {
     'A': '^>A',
     '^': '^A',
     '<': '<A',
     'v': 'A',
     '>': '>A'
}
arrow_pad['>'] = {
     'A': '^A',
     '^': '<^A',
     '<': '<<A',
     'v': '<A',
     '>': 'A'
}


def get_numeric_sequence(digit_start, digit_end, numeric_pad):
    return numeric_pad[digit_start][digit_end]


ALENGTH_CACHE = defaultdict(int)
def get_arrow_length(in_sequence, arrow_pad, levels):
    sequence = ''
    arrow_start = 'A'
    sequence_length = 0
    for arrow in in_sequence:
            if (arrow_start, arrow, levels) in ALENGTH_CACHE:
                sequence_length += ALENGTH_CACHE[(arrow_start, arrow, levels)]
            else:
                next_sequence = arrow_pad[arrow_start][arrow]
                if levels > 1:
                    next_sequence_length = get_arrow_length(next_sequence, arrow_pad, levels - 1)
                    sequence_length += next_sequence_length
                else:
                     next_sequence_length = len(next_sequence)
                     sequence_length += next_sequence_length
                ALENGTH_CACHE[(arrow_start, arrow, levels)] = next_sequence_length
            arrow_start = arrow
    return sequence_length




f = open('aoc21.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()


complexity = 0
for code in raw_input:
    digit_sequence = ''
    start_numeric = 'A'
    for digit in code:
        end_numeric = digit
        digit_sequence += get_numeric_sequence(start_numeric, end_numeric, numeric_pad)
        start_numeric = end_numeric
    sequence_length = get_arrow_length(digit_sequence, arrow_pad, 2)
    code_number = int(code[:-1])
    complexity += (code_number * sequence_length)

print('Part 1: total complexity is ' + str(complexity))
complexity = 0

for code in raw_input:
    digit_sequence = ''
    start_numeric = 'A'
    for digit in code:
        end_numeric = digit
        digit_sequence += get_numeric_sequence(start_numeric, end_numeric, numeric_pad)
        start_numeric = end_numeric
    sequence_length = get_arrow_length(digit_sequence, arrow_pad, 25)
    code_number = int(code[:-1])
    complexity += (code_number * sequence_length)
print('Part 2: total complexity is ' + str(complexity))
