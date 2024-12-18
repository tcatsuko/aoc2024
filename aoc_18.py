import networkx as nx

f = open('aoc18.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()

G = nx.Graph()

size = 71
bytes_to_fall = 1024
start_pos = (0,0)
end_pos = (size-1, size-1)

for row in range(size):
    for col in range(size):
        if row != 0:
            up_row = row - 1
            G.add_edge((row, col), (up_row, col))
        if row != (size - 1):
            down_row = row + 1
            G.add_edge((row, col), (down_row, col))
        if col != 0:
            left_col = col - 1
            G.add_edge((row, col), (row, left_col))
        if col != size - 1:
            right_col = col + 1
            G.add_edge((row, col), (row, right_col))

for node in range(bytes_to_fall):
    col, row = [int(x) for x in raw_input[node].split(',')]
    G.remove_node((row, col))
shortest_length = nx.shortest_path_length(G, start_pos, end_pos)
shortest_path = nx.shortest_path(G, start_pos, end_pos)
print('Part 1: shortest path is ' + str(shortest_length))

for x in range(bytes_to_fall + 1, len(raw_input)):
    col, row = [int(x) for x in raw_input[x].split(',')]
    G.remove_node((row, col))
    
    if (row, col) in shortest_path:
        has_path = nx.has_path(G, start_pos, end_pos)
        if has_path:
            shortest_path = nx.shortest_path(G, start_pos, end_pos)
        else:
            bad_byte = (row, col)
            break
print('Part 2: the bad byte is at ' + str(bad_byte[1]) + ',' + str(bad_byte[0]))
