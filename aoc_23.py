import networkx as nx
f = open('aoc23.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()

G = nx.Graph()
for line in raw_input:
    node1, node2 = line.split('-')
    G.add_edge(node1, node2)
t_sets = set()

for node in G.nodes:
    if node[0] == 't':
        edges = G.degree(node)
        if edges >=3:
            neighbors = list(G.neighbors(node))
            for x in range(len(neighbors) - 1):
                next_node = neighbors[x]
                possible_nodes = neighbors[x+1:]
                for third_node in possible_nodes:
                    if G.has_edge(next_node, third_node):
                        triplet = [node, next_node, third_node]
                        triplet.sort()
                        t_sets.add(tuple(triplet))
print('Part 1: there are ' + str(len(t_sets)) + ' triplets that contain a computer starting with t')

largest_neighbors = 0
largest_network = []
for node in G.nodes():
    neighbors = list(G.neighbors(node))
    for next_node in neighbors:
        common = list(nx.common_neighbors(G, node, next_node))
        net_count = 2 + len(common)
        if net_count > largest_neighbors:
            all_connected = True
            network = [node, next_node] + common
            for idx in range(len(network) - 1):
                current_node = network[idx] 
                for nn in network[idx + 1:]:
                    if not G.has_edge(current_node, nn):
                        all_connected = False
            if all_connected:
                largest_neighbors = net_count
                largest_network = network
largest_network.sort()
password = ','.join(largest_network)
print('Part 2: the password is ' + password)