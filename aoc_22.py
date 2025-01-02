from collections import defaultdict
f = open ('aoc22.txt','rt')
raw_input = []
for line in f:
    raw_input += [int(line[:-1])]
f.close()

def pseudorando(number):
    step1 = ((number * 64) ^ number) % 16777216
    step2 = (int(step1 / 32) ^ step1) % 16777216
    step3 = ((step2 * 2048) ^ step2) % 16777216
    return step3

secret_sum = 0
num_to_generate = 2000
pricechange_dict = defaultdict(list)
def check_zeroes(in_prices):
    # returns false if there are consecutive zeroes
    for i in range(len(in_prices) - 1):
        if in_prices[i] == 0 and in_prices[i + 1] == 0:
            return False
    return True

for number in raw_input:
    secret_number = number
    prev_offer = secret_number % 10
    last_four = []
    ind_pricechange = defaultdict(int)
    for _ in range(num_to_generate):
        secret_number = pseudorando(secret_number)
        current_offer = secret_number % 10
        if current_offer == 7:
            db = 1
        if len(last_four) < 4:
            last_four += [current_offer - prev_offer]
        else:
            last_four.pop(0)
            last_four += [current_offer - prev_offer]
            if last_four == [-2,1,-1,3]:
                db = 1
            if tuple(last_four) not in ind_pricechange:
                ind_pricechange[tuple(last_four)] = current_offer
        prev_offer = current_offer
    for key, value in ind_pricechange.items():
        pricechange_dict[key] += [value]
    secret_sum += secret_number
    

print('Part 1: sum of secret numbers is ' + str(secret_sum))

max_bananas = max([sum(x) for x in pricechange_dict.values()])
print('Part 2: max bananas the monkeys obtain is ' + str(max_bananas))