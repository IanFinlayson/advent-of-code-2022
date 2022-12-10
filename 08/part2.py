import sys

def read_input():
    grid = []
    for line in sys.stdin:
        row = []
        for cell in line[:-1]:
            row.append(int(cell))
        grid.append(row)
    return grid


def calculate_score(grid, i, j):
    us = grid[i][j]

    # look in each direction in turn
    north = 0
    move = i - 1
    while move >= 0:
        north += 1
        if grid[move][j] >= us:
            break
        move -= 1

    # look in each direction in turn
    south = 0
    move = i + 1
    while move < len(grid):
        south += 1
        if grid[move][j] >= us:
            break
        move += 1

    west = 0
    move = j - 1
    while move >= 0:
        west += 1
        if grid[i][move] >= us:
            break
        move -= 1

    east = 0
    move = j + 1
    while move < len(grid):
        east += 1
        if grid[i][move] >= us:
            break
        move += 1
    
    return north * south * east * west


# get the inputs
grid = read_input()

best = 0
for i in range(len(grid)):
    for j in range(len(grid)):
        score = calculate_score(grid, i, j)
        if score > best:
            best = score

print(best)

