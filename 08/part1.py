import sys

# make one pass through the lists
def make_pass(grid, visible, startx, starty, update, done):
    x = startx
    y = starty
    tallest = grid[y][x]
    while not done(x, y):
        if grid[y][x] > tallest:
            visible[y][x] = True
            tallest = grid[y][x]
        x, y = update(x, y)

def read_input():
    grid = []
    visible = []
    for line in sys.stdin:
        row = []
        vrow = []
        for cell in line[:-1]:
            row.append(int(cell))
            vrow.append(False)
        grid.append(row)
        visible.append(vrow)
    return grid, visible


# get the inputs
grid, visible = read_input()

# set all edges to visible
for i in range(len(grid)):
    visible[i][0] = True
    visible[i][len(grid) - 1] = True
    visible[0][i] = True
    visible[len(grid) - 1][i] = True

# make all the passes
for counter in range(len(grid)):
    # left to right
    make_pass(grid, visible, 0, counter, lambda x, y: (x+1, y), lambda x, y: x == len(grid))

    # right to left
    make_pass(grid, visible, len(grid) - 1, counter, lambda x, y: (x-1, y), lambda x, y: x < 0)
    
    # top to bottom
    make_pass(grid, visible, counter, 0, lambda x, y: (x, y+1), lambda x, y: y == len(grid))
    
    # bottom to top
    make_pass(grid, visible, counter, len(grid) - 1, lambda x, y: (x, y-1), lambda x, y: y < 0)


# count up the results
total = 0
for i in range(len(grid)):
    for j in range(len(grid)):
        if visible[i][j]:
            total += 1
print(total)


