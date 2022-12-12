import sys

# convert letters into numerical heights
def score(letter):
    return ord(letter) - ord('a')

# build out the grid and note start/end locations
def readInput():
    grid = []
    i = 0
    for line in sys.stdin:
        row = []
        j = 0
        for char in line[:-1]:
            if char == "S":
                row.append(0)
            elif char == "E":
                row.append(25)
                end = (i, j)
            else:
                row.append(score(char))
            j += 1
        grid.append(row)
        i += 1
    return grid, end

# we keep track of the tentative cost to get to each location
def initTentative(start):
    tentative = []
    for i in range(len(grid)):
        trow = []
        for j in range(len(grid[0])):
            trow.append(None)
        tentative.append(trow)
    # getting to start is free
    tentative[start[0]][start[1]] = 0
    return tentative

# choose smallest cost node from a list, and remove it
def popNext(nodes, tentative):
    best = None
    for (row, col) in nodes:
        if tentative[row][col] != None and (best == None or tentative[row][col] < bestCost):
            bestCost = tentative[row][col]
            best = (row, col)
    nodes.remove(best)
    return best

# consider if we can go in this direction or not
def consider(row, col, nrow, ncol, grid, tentative, nodes, direction):
    # check if we can get from here to there
    if (grid[row][col] + 1) >= grid[nrow][ncol]:
        distance = tentative[row][col] + 1
        # check if this is better than what we have
        if tentative[nrow][ncol] == None or distance < tentative[nrow][ncol]:
            tentative[nrow][ncol] = distance
            nodes.append((nrow, ncol))

def shortestPath(grid, start, end):
    tentative = initTentative(start)

    # keep track of locations we can visit
    nodes = [start]

    # while there are locations we can visit
    while len(nodes) > 0:
        row, col = popNext(nodes, tentative)
        if row > 0:
            consider(row, col, row - 1, col, grid, tentative, nodes, "North")
        if row < (len(grid) - 1):
            consider(row, col, row + 1, col, grid, tentative, nodes, "South")
        if col > 0:
            consider(row, col, row, col - 1, grid, tentative, nodes, "East")
        if col < (len(grid[0]) - 1):
            consider(row, col, row, col + 1, grid, tentative, nodes, "West")
    return tentative[end[0]][end[1]]

# load the data
grid, end = readInput()
bestCost = None

# find all the 0's
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 0:
            cost = shortestPath(grid, (i, j), end)
            if cost != None and (bestCost == None or cost < bestCost):
                bestCost = cost
print(bestCost)

