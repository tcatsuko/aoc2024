f = open('aoc11.txt','rt')
stones = []
for line in f:
    stones = [int(x) for x in line[:-1].split()]
f.close()
num_blinks = 75

for _ in range(num_blinks):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones += [1]
        elif len(str(stone)) % 2 == 0:
            stone_string = str(stone)
            stone_string_halflife = len(stone_string) // 2
            new_stones += [int(stone_string[:stone_string_halflife])]
            new_stones += [int(stone_string[stone_string_halflife:])]
        else:
            new_stones += [stone * 2024]
    stones = new_stones[:]
    db = 1
print('Part 1: there are ' + str(len(stones)) + ' stones now after ' + str(num_blinks) + ' blinks.')