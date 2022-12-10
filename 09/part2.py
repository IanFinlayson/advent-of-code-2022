import sys
import numpy as np

def fix(head, tail, hnum, tnum):
    # how off is the tail now?
    xdist = abs(head[0] - tail[0])
    xdir = np.sign(head[0] - tail[0])
    ydist = abs(head[1] - tail[1])
    ydir = np.sign(head[1] - tail[1])

    # if one dimension is off by 2, move it one step
    # AND if other dimension is off by 1 OR MORE, fix that too
    if xdist == 2:
        tail[0] += xdir
        if ydist >= 1:
            tail[1] += ydir
    elif ydist == 2:
        tail[1] += ydir
        if xdist >= 1:
            tail[0] += xdir

def trans(head, direction):
    if direction == "R":
        head[0] += 1
    elif direction == "L":
        head[0] -= 1
    elif direction == "U":
        head[1] += 1
    elif direction == "D":
        head[1] -= 1


def dump(knots):
    xmax = 0
    ymax = 0
    xmin = 0
    ymin = 0
    for knot in knots:
        if knot[0] > xmax:
            xmax = knot[0] + 2
        if knot[0] < xmin:
            xmin = knot[0] - 2
        if knot[1] > ymax:
            ymax = knot[1] + 2
        if knot[1] < ymin:
            ymin = knot[1] - 2
    grid = []
    for y in range(ymin, ymax + 1):
        line = []
        for x in range(xmin, xmax + 1):
            line.append(".")
        grid.append(line)
    grid[knots[0][1]][knots[0][0]] = "H"
    for i in range(9, 0, -1):
        grid[knots[i][1]][knots[i][0]] = str(i)
    grid.reverse()
    for line in grid:
        for spot in line:
            print(spot, end="")
        print()
    print()


knots = []
for i in range(10):
    knots.append([0, 0])
taillocs = {str(knots[9])}

for line in sys.stdin:
    direction, distance = line[:-1].split()
    for i in range(int(distance)):
        trans(knots[0], direction)
        for i in range(9):
            fix(knots[i], knots[i + 1], i, i + 1)
        #dump(knots)
        taillocs.add(str(knots[9]))

print(len(taillocs))

