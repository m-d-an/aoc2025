# %%
file = open('input.txt', 'r')

# %%
buttons = []

# %%
from itertools import combinations

def combinations_for_even_numbers(num_target):
    combs = []
    for r in range(len(buttons) + 1):
        combs.extend(combinations(buttons, r))

    valid_combinations = []
    for c in combs:
        odd = [False] * len(num_target)
        for b in c:
            for ni in b:
                odd[ni] = not odd[ni]
        if odd == num_target:
            #print(c, odd)
            valid_combinations.append(c)

    return valid_combinations

# %%
def compute_presses(jolts):
    if min(jolts) < 0:
        return 1000000
    if sum(jolts) == 0:
        return 0
    odd_values = [x % 2 == 1 for x in jolts]
    valid_cs = combinations_for_even_numbers(odd_values)

    if len(valid_cs) == 0:
        return 1000000
    
    presses = []
    for comb in valid_cs:
        new_jolts = jolts.copy()
        for b in comb:
            for ni in b:
                new_jolts[ni] = new_jolts[ni] - 1
        new_jolts = [int(x/2) for x in new_jolts]
        #print(jolts, comb, new_jolts)
        presses.append((2*compute_presses(new_jolts))+len(comb))
    #print(presses)
    return min(presses)

# %%
fewest_presses = 0
for line in file.readlines():
    s = line.strip().split(' ')

    # jolts
    jolt_target = []
    jolts = s[-1][1:-1].split(',')
    for j in jolts:
        jolt_target.append(int(j))
    #print(jolt_target)

    # buttons
    buttons = []
    for b in s[1:-1]:
        idxs = b[1:-1].split(',')
        for i in range(len(idxs)):
            idxs[i] = int(idxs[i])
        buttons.append(tuple(idxs))
    #print(buttons)

    presses = compute_presses(jolt_target)
    #print(jolt_target, buttons, presses)
    fewest_presses += presses

print(fewest_presses)


