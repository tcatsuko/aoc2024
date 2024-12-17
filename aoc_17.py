from collections import defaultdict
f = open('aoc17.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()

A = int(raw_input[0].split(': ')[1])
B = int(raw_input[1].split(': ')[1])
C = int(raw_input[2].split(': ')[1])
program = [int(x) for x in raw_input[4].split(': ')[1].split(',')]

pc = 0
output = []

def combo_operand(operand, A, B, C):
    if operand == 4:
        return A
    if operand == 5:
        return B
    if operand == 6:
        return C
    return operand
def run_program(A, B, C, program, pc = 0):
    output = []
    while pc < len(program):
        opcode = program[pc]
        pc += 1
        if opcode == 0:
            numerator = A
            operand = combo_operand(program[pc], A, B, C)
            denominator = 2 ** operand
            A = numerator // denominator
            pc += 1
        elif opcode == 1:
            operand = program[pc]
            B = B ^ operand
            pc += 1
        elif opcode == 2:
            operand = combo_operand(program[pc], A, B, C)
            B = operand % 8
            pc += 1
        elif opcode == 3:
            operand = program[pc]
            if A != 0:
                pc = operand
            else:
                pc += 1
        elif opcode == 4:
            B = B ^ C
            pc += 1
        elif opcode == 5:
            operand = combo_operand(program[pc], A, B, C)
            output += [operand % 8]
            pc += 1
        elif opcode == 6:
            numerator = A
            operand = combo_operand(program[pc], A, B, C)
            denominator = 2 ** operand
            B = numerator // denominator
            pc += 1
        elif opcode == 7:
            numerator = A
            operand = combo_operand(program[pc], A, B, C)
            denominator = 2 ** operand
            C = numerator // denominator
            pc += 1
    return output
output = run_program(A, B, C, program)
out_strings = [str(x) for x in output]
output = ','.join(out_strings)
print('Part 1: output is ' + output)
# The program operates on the lowest octal bit each loop. So begin by finding what
# the different octal bits output

possible_numbers = [0] # Start from scratch
for position in range(1, len(program) + 1):
    output = []
    for possible in possible_numbers:
        for offset in range(8): # 3-bit octet
            A = 8 * possible + offset
            out_vals = run_program(A, B, C, program)
            if out_vals == program[-position:]:
                output += [A]
    possible_numbers = output
print('Part 2: minimum value of A is ' + str(min(output)))
