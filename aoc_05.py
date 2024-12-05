f = open('aoc05.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
rules = []
pages = []
correct_pages = []
incorrect_pages = []
pages_begin = -1
for i, line in enumerate(raw_input):
    if line == '':
        pages_begin = i + 1
        break
    current_rule = line.split('|')
    rules += [current_rule]

for i in range(pages_begin, len(raw_input)):
    pages +=[[x for x in raw_input[i].split(',')]]

def out_of_order(update, rules):
    ooo = False
    changed_update = update[:]

    for page in update:
        applicable_rules = [x for x in rules if x[0] == page]
        for rule in applicable_rules:
            page_index = changed_update.index(page)
            if rule[1] in changed_update:
                rule_index = changed_update.index(rule[1])
                if page_index > rule_index:
                    page_to_move = changed_update.pop(page_index)
                    changed_update.insert(rule_index, page_to_move)
                    ooo = True
        db = 1
    update = changed_update[:]
    return (ooo, update)
for index in range(len(pages)):
    update = pages[index]
    ooo_test = out_of_order(update, rules)
    if ooo_test[0] == False:
        correct_pages += [update]
        continue
    while ooo_test[0]:
        update = ooo_test[1]
        ooo_test = out_of_order(update, rules)
    incorrect_pages += [ooo_test[1]]
middle_sum_correct = 0
for update in correct_pages:
    midpoint = len(update) // 2
    middle_sum_correct += int(update[midpoint])
print('Part 1: sum of middle pages is ' + str(middle_sum_correct))
middle_sum_incorrect = 0
for update in incorrect_pages:
    midpoint = len(update) // 2
    middle_sum_incorrect += int(update[midpoint])
print('Part 2: sum of middle pages is ' + str(middle_sum_incorrect))