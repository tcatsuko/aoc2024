import networkx as nx
f = open('test_aoc16.txt','rt')
for line in f:
    raw_input += [line[:-1]]
f.close()

G = nx.Graph()
rows = len(raw_input)
cols = len(raw_input[0])
for row, line in enumerate(raw_input):
    for col, node in enumerate(line):
        # Traverse the graph horizontally, note any turns and add them
        if node == '#':
            continue
        if node == 'S':
            start_node = (row, col)
        elif node == 'E':
            end_node = (row, col)
        can_move_left = False
        can_move_right = False
        can_move_up = False
        can_move_down = False
        if node[row][col - 1] == '.':
            G.add_edge((row, col - 1),(row, col), weight=1)
            can_move_horizontal = True
        if node[row][col + 1] == '.': 
            