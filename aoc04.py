f = open('test_aoc04.txt','rt')
raw_input = []
for line in f:
    raw_input += [line.strip()]
f.close()
# Pad the input
line_length = len(raw_input[0])
padded_line = '.' * line_length
raw_input = [padded_line, padded_line, padded_line] + raw_input + [padded_line, padded_line, padded_line]
wordsearch = []
for line in raw_input:
    wordsearch += ['...' + line + '...']
db = 1
found_xmas = 0
# Part 1
for row, line in enumerate(wordsearch):
    for col, letter in enumerate(line):
        if letter == 'X':
            # 1 2 3
            # 4 X 5
            # 6 7 8
            if wordsearch[row-1][col-1] == 'M' and wordsearch[row-2][col-2] == 'A' and wordsearch[row-3][col-3] == 'S':
                found_xmas += 1
            if wordsearch[row-1][col] == 'M' and wordsearch[row-2][col] == 'A' and wordsearch[row-3][col] == 'S':
                found_xmas += 1
            if wordsearch[row-1][col+1] == 'M' and wordsearch[row-2][col+2] == 'A' and wordsearch[row-3][col+3] == 'S':
                found_xmas += 1
            if wordsearch[row][col-1] == 'M' and wordsearch[row][col-2] == 'A' and wordsearch[row][col-3] == 'S':
                found_xmas += 1
            if wordsearch[row][col+1] == 'M' and wordsearch[row][col+2] == 'A' and wordsearch[row][col+3] == 'S': 
                found_xmas += 1
            if wordsearch[row+1][col-1] == 'M' and wordsearch[row+2][col-2] == 'A' and wordsearch[row+3][col-3] == 'S':
                found_xmas += 1
            if wordsearch[row+1][col] == 'M' and wordsearch[row+2][col] == 'A' and wordsearch[row+3][col] == 'S':
                found_xmas += 1
            if wordsearch[row+1][col+1] == 'M' and wordsearch[row+2][col+2] == 'A' and wordsearch[row+3][col+3] == 'S':
                found_xmas += 1
print('Part 1: found ' + str(found_xmas) + ' instances of XMAS')