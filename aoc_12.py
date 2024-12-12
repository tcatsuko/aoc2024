import networkx as nx

f = open('aoc12.txt','rt')
raw_input = []
for line in f:
    raw_input += [[x for x in line[:-1]]]
f.close()
garden = []
rows = len(raw_input)
cols = len(raw_input[0])
padding = ['.'] * cols
raw_input = [padding] + raw_input + [padding]
for line in raw_input:
    garden += [['.'] + line + ['.']]
G = nx.Graph()
plant_nodes = []

for row, line in enumerate(garden):
    for col, plot in enumerate(line):
        has_neighbor = False
        perimeter = 0
        if plot == '.':
            continue
        plant_nodes += [(row, col)]
        if garden[row - 1][col] == plot:
            G.add_edge((row, col),(row-1, col))
            has_neighbor = True
        if garden[row+1][col] == plot:
            G.add_edge((row, col),(row+1, col))
            has_neighbor = True
        if garden[row][col - 1] == plot:
            G.add_edge((row, col),(row, col-1))
            has_neighbor = True
        if garden[row][col + 1] == plot:
            G.add_edge((row, col), (row, col+1))
            has_neighbor = True
        if not has_neighbor:
            G.add_node((row, col))

def reachable(G, start):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            queue.extend(G.neighbors(node))
    return visited
def get_perimeter(garden, plants):
    perimeter = 0
    for plant in plants:
        row = plant[0]
        col = plant[1]
        plant_type = garden[row][col]
        if garden[row-1][col] != plant_type:
            perimeter += 1
        if garden[row+1][col] != plant_type:
            perimeter += 1
        if garden[row][col-1] != plant_type:
            perimeter += 1
        if garden[row][col+1] != plant_type:
            perimeter += 1
    return perimeter
def get_sides(garden, plants):
    # get top sides:
    top_plants = list(plants)[:]
    top_plants.sort()
    current_row = [x for x in top_plants if x[0] == top_plants[0][0]]
    sides = 0
    
    while top_plants:
        for x in current_row:
            top_plants.remove(x)
        boundary = False
        for plant in current_row:
            row = plant[0]
            col = plant[1]
            plant_type = garden[row][col]
            
            if boundary == False and garden[row-1][col] != plant_type:
                boundary = True
            if garden[row-1][col] == plant_type and boundary == True:
                boundary = False
                sides += 1
            if garden[row][col + 1] != plant_type and boundary == True:
                boundary = False
                sides += 1
        
        current_row = [x for x in top_plants if x[0] == top_plants[0][0]]
    # get bottom sides:
    bottom_plants = list(plants)[:]
    bottom_plants.sort()
    current_row = [x for x in top_plants if x[0] == bottom_plants[0][0]]
    
    
    while bottom_plants:
        for x in current_row:
            bottom_plants.remove(x)
        boundary = False
        for plant in current_row:
            row = plant[0]
            col = plant[1]
            plant_type = garden[row][col]
            
            if boundary == False and garden[row+1][col] != plant_type:
                boundary = True
            if garden[row+1][col] == plant_type and boundary == True:
                boundary = False
                sides += 1
            if garden[row][col + 1] != plant_type and boundary == True:
                boundary = False
                sides += 1
        
        current_row = [x for x in bottom_plants if x[0] == bottom_plants[0][0]]


    # get left sides:
    left_plants = list(plants)[:]
    left_plants.sort()
    current_row = [x for x in left_plants if x[1] == left_plants[0][1]]
    current_row.sort()
    
    while left_plants:
        for x in current_row:
            left_plants.remove(x)
        boundary = False
        for plant in current_row:
            row = plant[0]
            col = plant[1]
            plant_type = garden[row][col]
            
            if boundary == False and garden[row][col - 1] != plant_type:
                boundary = True
            if garden[row][col - 1] == plant_type and boundary == True:
                boundary = False
                sides += 1
            if garden[row + 1][col] != plant_type and boundary == True:
                boundary = False
                sides += 1
        
        current_row = [x for x in left_plants if x[1] == left_plants[0][1]]
        current_row.sort()

    # get right sides:
    right_plants = list(plants)[:]
    right_plants.sort()
    current_row = [x for x in right_plants if x[1] == right_plants[0][1]]
    current_row.sort()
    
    while right_plants:
        for x in current_row:
            right_plants.remove(x)
        boundary = False
        for plant in current_row:
            row = plant[0]
            col = plant[1]
            plant_type = garden[row][col]
            
            if boundary == False and garden[row][col + 1] != plant_type:
                boundary = True
            if garden[row][col + 1] == plant_type and boundary == True:
                boundary = False
                sides += 1
            if garden[row + 1][col] != plant_type and boundary == True:
                boundary = False
                sides += 1
        
        current_row = [x for x in right_plants if x[1] == right_plants[0][1]]
        current_row.sort()
    return sides

total_price_p1 = 0
total_price_p2 = 0
while plant_nodes:
    start = plant_nodes[0]
    can_reach = reachable(G, start)
    area = len(can_reach)
    perimeter = get_perimeter(garden, can_reach)
    sides = get_sides(garden, can_reach)
    for plant in can_reach:
        plant_nodes.remove(plant)
    total_price_p1 += (area * perimeter)
    total_price_p2 += (area * sides)
print('Part 1: total price is ' + str(total_price_p1))
print('Part 2: total price is ' + str(total_price_p2))