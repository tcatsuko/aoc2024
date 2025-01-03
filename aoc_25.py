f = open('aoc25.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()

locks = []
keys = []
current_item = []
start_item = False
is_lock = False
for line in raw_input:
    if line == '':
        if is_lock:
            locks += [current_item]
        else:
            keys += [current_item]
        current_item = []
        start_item = False
        is_lock = False
        continue
    if start_item == False and (line == '#####'):
        start_item = True
        is_lock = True
    elif start_item == False and line == '.....':
        start_item = True
        is_lock = False
        
    current_item += [[x for x in line]]
if is_lock:
    locks += [current_item]
else:
    keys += [current_item]
keynum = []
locknum = []
for lock in locks:
    current_lock = []
    transpose_lock = list(map(list, zip(*lock)))
    for line in transpose_lock:
        current_lock += [line.count('.')]
    locknum += [current_lock]
for key in keys:
    current_key = []
    transpose_key = list(map(list, zip(*key)))
    for line in transpose_key:
        current_key += [line.count('#') - 1]
    keynum += [current_key]
fit_keys = 0

for lock in locknum:
    for key in keynum:
        can_fit = True
        for i in range(5):
            if key[i] >= lock[i]:
                can_fit = False
        if can_fit:
            fit_keys += 1
print('Part 1: ' + str(fit_keys) + ' keys fit.')