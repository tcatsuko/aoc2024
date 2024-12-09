f = open('aoc09.txt','rt')
raw_input = []
for line in f:
    raw_input += [int(x) for x in line[:-1]]
f.close()
total_disk_size = sum(raw_input)
# Build table of ids
files = []
space = []

for x in range(0, len(raw_input), 2):
    blocks = raw_input[x]
    id = x // 2
    files += [blocks]
    if x <= len(raw_input) - 3:
        space += [raw_input[x+1]]
disk = []
original_files = files[:]
left_filenum = 0
right_filenum = len(files) - 1
spotnum = 0
left_file = True
while True:
    if left_file:
        file_blocks = files.pop(0)
        filenum = left_filenum
        for y in range(file_blocks):
            disk += [filenum]
        left_filenum += 1
        left_file = False
    else:
        free_space = space.pop(0)
        while free_space > 0:
            if len(files) == 0:
                break
            right_fileblocks = files[-1]
            if right_fileblocks == 0:
                files.pop(-1)
                right_filenum -= 1
            else:
                disk += [right_filenum]
                files[-1] -= 1
                free_space -= 1
        left_file = True
    if len(files) == 0:
        break
def calculate_checksum(my_disk):
    checksum = 0
    for index, filenum in enumerate(my_disk):
        if filenum != -1:
            checksum += (index * filenum)
    return checksum
disk_checksum = calculate_checksum(disk)
print('Part 1: checksum is ' + str(disk_checksum))

# Part 2
files = []
space = []
offset = 0
for x in range(0, len(raw_input), 2):
    blocks = raw_input[x]
    id = x // 2
    files += [(offset, id, blocks)]
    offset += blocks
    if x <= len(raw_input) - 3:
        space += [(offset, raw_input[x+1])]
        offset += raw_input[x+1]      

reversed_files = files[::-1]

for idx, disk_file in enumerate(reversed_files[:-1]):
    file_offset = disk_file[0]
    file_id = disk_file[1]
    file_blocks = disk_file[2]
    empty_space_blocks = [x for x in space if x[1] >= file_blocks]
    if len(empty_space_blocks) > 0:
        first_space_block = empty_space_blocks[0]
        first_space_idx = space.index(first_space_block)
        if first_space_block[0] > file_offset:
            continue
        new_disk_file = (first_space_block[0], disk_file[1], disk_file[2])
        reversed_files[idx] = new_disk_file
        new_space_avail = first_space_block[1] - file_blocks
        new_space_block = (first_space_block[0] + file_blocks, first_space_block[1] - file_blocks)
        space[first_space_idx] = new_space_block
        if idx > 0 and idx < len(reversed_files) - 1:
            space = space[::-1]
            space[idx + 1] = (space[idx][0], space[idx][1] + space[idx+1][1])
            space[idx] = (space[idx + 1][0], 0)
            space = space[::-1]
        elif idx == 0:
            if space[-1][0] != disk_file[0] and space[-1][0] < reversed_files[1][0]:
                space += [(disk_file[0], file_blocks)]
            elif space[-1][0] != disk_file[0] and space[-1][0] > reversed_files[1][0]:
                space[-1] = (space[-1][0], space[-1][1] + file_blocks)

            
def part2_checksum(file_info):
    checksum = 0
    for my_file in file_info:
        offset_start = my_file[0]
        file_id = my_file[1]
        file_length = my_file[2]
        for x in range(file_length):
            offset = offset_start + x
            checksum += offset * file_id
    return checksum    
new_checksum = part2_checksum(reversed_files)
print('Part 2: checksum is ' + str(new_checksum))


