import networkx as nx
f = open('aoc16.txt','rt')
raw_input = []
for line in f:
    raw_input += [[x for x in line[:-1]]]
f.close()

G = nx.DiGraph()

same_dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for row, line in enumerate(raw_input):
    for col, node in enumerate(line):
        # Traverse the graph horizontally, note any turns and add them
        # 0: E
        # 1: S
        # 2: W
        # 3: N
        # Directions = [(0,1), (1, 0), (0, -1), (-1,0)]
        if node == '#':
            continue
        if node == 'S':
            start_node = (row, col,0)

        elif node == 'E':
            end_node = (row, col, 0)
        for x in range(4):
            G.add_node((row, col, x))
for node in list(G.nodes()):
    row = node[0]
    col = node[1]
    direction = node[2]
    dr,dc = same_dir[direction]
    # if (row + next_dir[0], col + next_dir[1], direction) in G.nodes:
    #     G.add_edge(node, (row + next_dir[0], col + next_dir[1], direction), weight=1)
    if (row + dr, col + dc, direction) in G.nodes:
        G.add_edge(node, (row + dr, col + dc, direction), weight=1)
    for x in range(4):
        G.add_edge(node, (row, col, x), weight=1000)


        
shortest_path = nx.shortest_path(G, start_node, end_node, weight='weight')
path_score = nx.path_weight(G, shortest_path, 'weight')
print('Part 1: Lowest score is ' + str(path_score))


best_tiles = set()
for path in nx.all_shortest_paths(G, start_node, end_node, weight='weight'):
        for node in path:
            best_tiles.add((node[0], node[1]))
print('Part 2: there are ' + str(len(best_tiles)) + ' best tiles in the map')

      
            