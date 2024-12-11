from collections import defaultdict
f = open('aoc11.txt','rt')
for line in f:
    stones_list = [int(x) for x in line[:-1].split()]
f.close()
num_blinks = 75

stones = defaultdict(int)
for stone in stones_list:
    stones[stone] += 1
    
for blink in range(num_blinks):
    if blink == 25: # 25th blink
        print('Part 1: there are ' + str(num_of_stones) + ' stones now after ' + str(blink) + ' blinks.')
    new_stones = defaultdict(int)
    
    for stone in stones:
        num_of_stones = stones[stone]
        
        
        if stone == 0:
            new_stones[1] += num_of_stones
        elif len(str(stone)) % 2 == 0:
            stone_string = str(stone)
            stone_string_length = len(stone_string) // 2
            new_stones[int(stone_string[:stone_string_length])] += num_of_stones
            new_stones[int(stone_string[stone_string_length:])] += num_of_stones
        else:
            new_stones[stone * 2024] += num_of_stones
    stones = new_stones.copy()
    db = 1
    num_of_stones = sum(stones.values())
print('Part 2: there are ' + str(num_of_stones) + ' stones now after ' + str(num_blinks) + ' blinks.')