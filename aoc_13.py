f = open('aoc13.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()

def solve_game(button_a, button_b, prize, offset = 0):
    ax = button_a[0]
    ay = button_a[1]
    bx = button_b[0]
    by = button_b[1]
    px = prize[0] + offset
    py = prize[1] + offset
    det = ((ax * by) - (ay * bx))
    a = (px * by - py * bx) / det
    b = (ax * py - ay * px) / det
    if int(a) == a and int(b) == b:
        return(int(a),int(b))
    else:
        return False
    

games = []
gamelist = raw_input[:]
while len(gamelist) >= 4:
    current_game = gamelist[:4]
    gamelist = gamelist[4:]
    button_a_text = current_game[0]
    button_b_text = current_game[1]
    prize_text = current_game[2]
    button_a = (int(button_a_text.split(': ')[1].split(', ')[0][1:]), int(button_a_text.split(': ')[1].split(', ')[1][1:]))
    button_b = (int(button_b_text.split(': ')[1].split(', ')[0][1:]), int(button_b_text.split(': ')[1].split(', ')[1][1:]))
    prize = (int(prize_text.split(': ')[1].split(', ')[0][2:]), int(prize_text.split(': ')[1].split(', ')[1][2:]))
    games += [[button_a, button_b, prize]]
current_game = gamelist[:]

button_a_text = current_game[0]
button_b_text = current_game[1]
prize_text = current_game[2]
button_a = (int(button_a_text.split(': ')[1].split(', ')[0][1:]), int(button_a_text.split(': ')[1].split(', ')[1][1:]))
button_b = (int(button_b_text.split(': ')[1].split(', ')[0][1:]), int(button_b_text.split(': ')[1].split(', ')[1][1:]))
prize = (int(prize_text.split(': ')[1].split(', ')[0][2:]), int(prize_text.split(': ')[1].split(', ')[1][2:]))
games += [[button_a, button_b, prize]]

coins = 0

    
for game in games:
    param1= game[0]
    param2 = game[1]
    prize = game[2]
    solved = solve_game(param1, param2, prize)
    if solved:
        coins += (3 * solved[0]) + solved[1]
   
print('Part 1: you need ' + str(coins) + ' tokens')
coins = 0
offset = 10000000000000
for game in games:
    param1= game[0]
    param2 = game[1]
    prize = game[2]
    solved = solve_game(param1, param2, prize, offset)
    if solved:
        coins += (3 * solved[0]) + solved[1]
print('Part 2: you need ' + str(coins) + ' tokens')