import networkx as nx

f = open('aoc24.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
# Parse out wires with known inputs
wires = {}
G = nx.Graph()

for idx, line in enumerate(raw_input):
    if line == '':
        gate_desc = idx + 1
        break
    wirename, wireval = line.split(': ')
    wires[wirename] = ('VAL', int(wireval), 1)
for line in raw_input[gate_desc:]:
    inputs, output = line.split(' -> ')
    in1, op, in2 = inputs.split(' ')
    G.add_edge(output, in1)
    G.add_edge(output, in2)
    wires[output] = (op, in1, in2)
wirecopy = wires.copy()
outputs = {}
z_wires = [x for x in wires.keys() if x[0] == 'z']
x_wires = [x for x in wires.keys() if x[0] == 'x']
y_wires = [x for x in wires.keys() if x[0] == 'y']
x_wires.sort()
y_wires.sort()
x_vals = []
y_vals = []

def build_operations(input_wire, wires):
    inputs = wires[input_wire]
    if inputs[0] == 'VAL':
        return inputs[1]
    elif inputs[0] == 'OR':
        operation = build_operations(inputs[1], wires) | build_operations(inputs[2], wires)
        wires[input_wire] = ('VAL', operation, 1)
        return operation
    elif inputs[0] == 'AND':
        operation = build_operations(inputs[1], wires) & build_operations(inputs[2], wires)
        wires[input_wire] = ('VAL', operation, 1)
        return operation
    elif inputs[0] == 'XOR': 
        operation = build_operations(inputs[1], wires) ^ build_operations(inputs[2], wires)
        wires[input_wire] = ('VAL', operation, 1)
        return operation

z_wires.sort()
def build_binary(wirelist, wires):
    opchain = ''
    for wire in wirelist:
        opchain += str(wires[wire][1])
    return opchain

for z_wire in z_wires:
    _ = build_operations(z_wire, wires)
z_wires.reverse()
output_bits = ''
output_bits = build_binary(z_wires, wires)

output = int(output_bits, 2)
print('part 1: ' + str(output))
wires = wirecopy.copy()
# Start the great renaming
aliases = {}

def get_key(dict, item):
    for key, value in dict.items():
        if value == item:
            return key
    return None
def swap_order(dict, key):
    item = dict[key]
    item_left = item[1]
    item_right = item[2]
    item_op = item[0]
    dict[key] = (item_op, item_right, item_left)

# Start by renaming the x and y ANDs
for idx in range(45):
    longnum = '%02d' % idx
    x_name = 'x' + longnum
    y_name = 'y' + longnum
    #is this already in the proper otder?
    andkey = get_key(wires, ('AND', x_name, y_name)) 
    if andkey == None:
        andkey = get_key(wires, ('AND', y_name, x_name))
        swap_order(wires, andkey)
    aliases['AND' + longnum] = andkey
    for key, value in wires.items():
        if andkey in value:
            i = value.index(andkey)
            listvalue = list(value)
            listvalue[i] = 'AND' + longnum
            wires[key] = tuple(listvalue)
    value = wires[andkey]
    wires['AND' + longnum] = value
    del wires[andkey]
    db = 1
    xorkey = get_key(wires, ('XOR', x_name, y_name))
    if xorkey == None:
        xorkey = get_key(wires, ('XOR', y_name, x_name))
        swap_order(wires, xorkey)
    aliases['XOR' + longnum] = xorkey
    for key, value in wires.items():
        if xorkey in value:
            i = value.index(xorkey)
            listvalue = list(value)

            listvalue[i] = 'XOR' + longnum

            wires[key] = tuple(listvalue)
    value = wires[xorkey]
    wires['XOR' + longnum] = value
    del wires[xorkey]
    db = 1
swaps = []

# Now rename AND00 to CARRY00
aliases['CARRY00'] = 'AND00'
for key, value in wires.items():
    if 'AND00' in value:
        listvalue = list(value)
        i = listvalue.index('AND00')
        listvalue[i] = 'CARRY00'
        wires[key] = tuple(listvalue)
value = wires['AND00']
wires['CARRY00'] = value
del wires['AND00']
# Now start to march down the field
for idx in range(1, 45):
    longnum = '%02d' % idx
    xorname = 'XOR' + longnum
    andname = 'AND' + longnum
    # check the xor and and
    xorval = wires[xorname]
    andval = wires[andname]
    print(str(xorval) + ' -> ' + xorname + ' (alias ' + aliases[xorname] + ')')
    print(str(andval) + ' -> ' + andname + ' (alias ' + aliases[andname] + ')')
    zkey = None
    for key, value in wires.items():
        if 'XOR' + longnum in value and 'XOR' in value:
            zkey = key
            zval = value
            break
    print(str(zval) + ' -> ' + zkey)
    for key, value in wires.items():
        if 'XOR' + longnum in value and 'AND' in value:
            carry_i_key = key
            carry_i_value = value
            break
    aliases['CARRY_I_' + longnum] = carry_i_key
    for key, value in wires.items():
        if carry_i_key in value:
            listvalue = list(value)
            i = listvalue.index(carry_i_key)
            listvalue[i] = 'CARRY_I_' + longnum
            wires[key] = tuple(listvalue)
    tempval = wires[carry_i_key]
    wires['CARRY_I_' + longnum] = tempval
    del wires[carry_i_key]
    print(str(wires['CARRY_I_' + longnum]) + ' -> CARRY_I_' + longnum + ' (alias ' + aliases['CARRY_I_' + longnum] + ')')
    
    for key, value in wires.items():
        if 'AND' + longnum in value and 'OR' in value:
            carry_key = key
            carry_value = value
            break
    aliases['CARRY' + longnum] = carry_key
    for key, value in wires.items():
        if carry_key in value:
            listvalue = list(value)
            i = listvalue.index(carry_key)
            listvalue[i] = 'CARRY' + longnum
            wires[key] = tuple(listvalue)
    tempval = wires[carry_key]
    wires['CARRY' + longnum] = tempval
    del wires[carry_key]
    print(str(wires['CARRY' + longnum]) + ' -> CARRY' + longnum + ' (alias ' + aliases['CARRY' + longnum] + ')')
    print()
    db = 1
# by manual inspection
swapped_wires = ['cdj','z08', 'z16','mrb','z32','gfm','dhm','qjd']
swapped_wires.sort()
print('Part 2: ' + ','.join(swapped_wires))
# Check the addition

for idx in range(45):
    longnum = '%02d' % idx
    x_key = 'x' + longnum
    y_key = 'y' + longnum



    
    