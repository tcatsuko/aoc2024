import networkx as nx
from collections import defaultdict

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
cheats = defaultdict(int)
cheat_distance = 2
for i, node in enumerate(shortest_path):
    possible_cheats = [x for x in shortest_path[i:] if manhattan_distance(node, x) <= cheat_distance and manhattan_distance(node, x) > 0]
    for next_node in possible_cheats:
        next_index = shortest_path.index(next_node)
        time_saved = abs(i - next_index) - manhattan_distance(node, next_node)
       
        cheats[time_saved] += 1
# NOTE: cheat counts will be doubled since we are counting from both start and end nodes
goal_time_saved = 100
goal_cheats = [x for x in cheats.keys() if x >= goal_time_saved]
num_goal_cheats = 0
for item in goal_cheats:
    num_goal_cheats += cheats[item]
print('Part 1: there are ' + str(num_goal_cheats) + ' cheats that save at least ' + str(goal_time_saved) + ' seconds.')

cheats = defaultdict(int)
# Part 2
cheat_distance = 20
for i, node in enumerate(shortest_path):
    
    possible_cheats = [x for x in shortest_path[i:] if manhattan_distance(node, x) <= cheat_distance and manhattan_distance(node, x) > 0]
    for next_node in possible_cheats:
        next_index = shortest_path.index(next_node)
        time_saved = abs(i - next_index) - manhattan_distance(node, next_node)
        
        cheats[time_saved] += 1
    print(str(i) + '/' + str(len(shortest_path)))
# NOTE: cheat counts will be doubled since we are counting from both start and end nodes
goal_time_saved = 100
goal_cheats = [x for x in cheats.keys() if x >= goal_time_saved]
num_goal_cheats = 0
for item in goal_cheats:
    num_goal_cheats += cheats[item]
print('Part 2: there are ' + str(num_goal_cheats) + ' cheats that save at least ' + str(goal_time_saved) + ' seconds.')

