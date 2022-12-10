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

score = 0
for line in sys.stdin:
    them, us = map(trans, line.split())
    score += us
    score += beats(us, them)

print(score)


