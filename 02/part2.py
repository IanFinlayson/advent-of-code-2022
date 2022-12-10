import sys

def trans(c):
    if c in "AX":
        return 1
    elif c in "BY":
        return 2
    elif c in "CZ":
        return 3

def beats(us, them):
    table = [[3, 0, 6],
             [6, 3, 0],
             [0, 6, 3]]
    return table[us - 1][them - 1]

def our_move(them, outcome):
    table = [[3, 1, 2],
             [1, 2, 3],
             [2, 3, 1]]
    return table[outcome - 1][them - 1]

score = 0
for line in sys.stdin:
    them, outcome = map(trans, line.split())
    us = our_move(them, outcome)
    score += us
    score += beats(us, them)

print(score)


