import networkx as nx

f = open('aoc10.txt','rt')
raw_input = []
for line in f:
    raw_input += [[int(x) for x in line[:-1]]]
f.close()
# Pad the graph
rows = len(raw_input)
cols = len(raw_input[0])
buffer = [-1] * cols
raw_input = [buffer] + raw_input + [buffer]
topo_map = []
for row in raw_input:
    row = [-1] + row + [-1]
    topo_map += [row]
trailheads = []
trailtails = []
rows += 2
cols += 2
G = nx.DiGraph()
for row , line in enumerate(topo_map):
    for col, node in enumerate(line):
        if node == 0:
            trailheads += [(row, col)]
        elif node == 9:
            trailtails += [(row, col)]
        if node == -1:
            # boundary
            continue
        # check directions:
        if topo_map[row - 1][col] - node == 1:
            G.add_edge((row, col), (row-1, col))
        if topo_map[row + 1][col] - node == 1:
            G.add_edge((row, col), (row + 1, col))
        if topo_map[row][col -1 ] - node == 1:
            G.add_edge((row, col), (row, col - 1))
        if topo_map[row][col + 1] - node == 1:
            G.add_edge((row, col), (row, col + 1))
# Now march the trailheads
scores = 0
for head in trailheads:
    trailhead_score = 0
    for tail in trailtails:
        if nx.has_path(G, head, tail):
            trailhead_score += 1
    scores += trailhead_score
print('Part 1: total score is ' + str(scores))

scores = 0
for head in trailheads:
    trailhead_score = 0
    for tail in trailtails:
        if nx.has_path(G, head, tail):
            trailhead_score += len(list(nx.all_simple_paths(G, head, tail)))
            db = 1
    scores += trailhead_score
print('Part 2: total ratings is ' + str(scores))