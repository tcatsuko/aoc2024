f = open('aoc07.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
equations = {}
for line in raw_input:
    split_line = line.split(': ')
    end_value = int(split_line[0])
    operands = [int(x) for x in split_line[1].split()]
    equations[end_value] = operands
operators = ['+','*']
bad_equations = {}
def calculate(initial_values, remaining_operands, operators):
    values_to_return = []
    next_operand = remaining_operands.pop(0)
    for value in initial_values:
        for operator in operators:
            if operator == '+':
                values_to_return += [value + next_operand]
            if operator == '*':
                values_to_return += [value * next_operand]
            if operator == '||':
                values_to_return += [int(str(value) + str(next_operand))]
    if len(remaining_operands) == 0:
        return values_to_return
    else:
        return calculate(values_to_return, remaining_operands, operators)
total_calibration = 0
for result in equations:
    operands = equations[result]
    possibilities = calculate([operands[0]], operands[1:], operators)
    if result in possibilities:
        total_calibration += result
    else:
        bad_equations[result] = equations[result]
print('Part 1: total calibration is ' + str(total_calibration))

# Part 2, only need to test the equations that did not work in part 1
extra_calibration = 0
operators += ['||']
for result in bad_equations:
    operands = bad_equations[result]
    possibilities = calculate([operands[0]], operands[1:], operators)
    if result in possibilities:
        extra_calibration += result
print('Part 1: total calibration is ' + str(total_calibration + extra_calibration))