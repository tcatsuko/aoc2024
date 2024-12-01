f = open('aoc01.txt','rt')
raw_input = []
for line in f:
    raw_input += [line.strip()]
f.close()
left_list = []
right_list = []
for line in raw_input:
    split_line = line.split('   ')
    left_list += [int(split_line[0])]
    right_list += [int(split_line[1])]
left_list.sort()
right_list.sort()
total_distance = 0
for x in range(len(left_list)):
    total_distance += abs(left_list[x] - right_list[x])
print('Part 1: total distance is ' + str(total_distance))
similarity_score = 0
for number in left_list:
    num_count = right_list.count(number)
    similarity_score += (number * num_count)
print('Part 2: similarity score is ' + str(similarity_score))