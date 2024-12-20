import networkx as nx

f = open('aoc20.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
G = nx.Graph()

def manhattan_distance(n1, n2):
    return abs(n1[0] - n2[0]) + abs(n1[1]-n2[1])

for row, line in enumerate(raw_input):
    for col, node in enumerate(line):
        if node != '#':
            if node == 'S':
                start_node = (row, col)
            if node == 'E':
                end_node = (row, col)
            if raw_input[row-1][col] != '#':
                G.add_edge((row, col),(row-1, col))
            if raw_input[row+1][col] != '#':
                G.add_edge((row, col),(row+1, col))
            if raw_input[row][col-1] != '#':
                G.add_edge((row, col),(row, col-1))
            if raw_input[row][col+1] != '#':
                G.add_edge((row, col), (row,col+1))
shortest_path = list(nx.shortest_path(G, start_node, end_node))
p1_cheat_distance = 2
p2_cheat_distance = 20
p1_cheats = 0
p2_cheats = 0
goal_time_saved = 100
for i, node in enumerate(shortest_path):
    possible_cheats = [x for x in shortest_path[i:] if manhattan_distance(node, x) <= p2_cheat_distance and manhattan_distance(node, x) > 0]
    for next_node in possible_cheats:
        distance = manhattan_distance(node, next_node)
        next_index = shortest_path.index(next_node)
        time_saved = abs(i - next_index) - distance
        if time_saved >= goal_time_saved:
            if distance == p1_cheat_distance:
                p1_cheats += 1
            p2_cheats += 1
       
print('Part 1: there are ' + str(p1_cheats) + ' cheats that save at least ' + str(goal_time_saved) + ' seconds.')
print('Part 2: there are ' + str(p2_cheats) + ' cheats that save at least ' + str(goal_time_saved) + ' seconds.')

