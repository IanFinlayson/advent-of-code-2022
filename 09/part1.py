import sys
import numpy as np

def trans(head, tail, direction):
    # take care of the head
    if direction == "R":
        head[0] += 1
    elif direction == "L":
        head[0] -= 1
    elif direction == "U":
        head[1] += 1
    elif direction == "D":
        head[1] -= 1

    # how off is the tail now?
    xdist = abs(head[0] - tail[0])
    xdir = np.sign(head[0] - tail[0])
    ydist = abs(head[1] - tail[1])
    ydir = np.sign(head[1] - tail[1])

    # if one dimension is off by 2, move it one step
    # AND if other dimension is off by 1, fix that too
    if xdist == 2:
        tail[0] += xdir
        if ydist == 1:
            tail[1] += ydir
    elif ydist == 2:
        tail[1] += ydir
        if xdist == 1:
            tail[0] += xdir

head = [0, 0]
tail = [0, 0]
taillocs = {str(tail)}

for line in sys.stdin:
    direction, distance = line[:-1].split()
    for i in range(int(distance)):
        trans(head, tail, direction)
        taillocs.add(str(tail))

print(len(taillocs))

