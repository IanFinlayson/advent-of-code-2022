import sys

stacks = [[] for i in range(10)]

def add_crates(line):
    for i in range(len(line)):
        if line[i].isupper():
            stacks[i // 4].append(line[i])


def process_move(amt, src, dest):
    moved = []
    for i in range(amt):
        crate = stacks[src - 1].pop(0)
        moved.append(crate)
    
    moved.reverse()
    for move in moved:
        stacks[dest - 1].insert(0, move)


def process_line(line):
    words = line.split()
    process_move(int(words[1]), int(words[3]), int(words[5]))

firstPart = True
for line in sys.stdin:
    if firstPart:
        if len(line) < 2:
            firstPart = False
        else:
            add_crates(line[:-1])
    else:
        process_line(line[:-1])

for s in stacks:
    if len(s) > 0:
        print(s[0], end="")
print()

