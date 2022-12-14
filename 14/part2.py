import sys
from numpy import sign

# this returns a list containing lines
# each line consists of a list of [x, y] pairs
def readInput():
    lines = []
    for line in sys.stdin:
        coords = line[:-1].split(" -> ")
        linecoords = []
        for coord in coords:
            x, y = map(int, coord.split(","))
            linecoords.append([x, y])
        lines.append(linecoords)
    return lines

# this returns the boundaries of the region given in the input
def getBounds(lines):
    # start with the first one (except minY which is always 0)
    minX = maxX = lines[0][0][0]
    maxY = lines[0][0][1]

    # check all the rest
    for line in lines:
        for coord in line:
            minX = min(minX, coord[0])
            maxX = max(maxX, coord[0])
            maxY = max(maxY, coord[1])
    return minX, maxX, 0, maxY

# build out the grid and return it
def buildGrid(lines, minX, maxX, minY, maxY):
    # start empty
    grid = []
    for y in range((maxY - minY) + 1):
        row = []
        for x in range((maxX - minX) + 1):
            row.append(".")
        grid.append(row)

    # put in the lines
    for line in lines:
        # for each segment in the line
        for i in range(len(line) - 1):
            start = line[i]
            end = line[i + 1]

            # draw the whole thing
            while start != end:
                grid[start[1] - minY][start[0] - minX] = "#"
                xinc = sign(end[0] - start[0])
                yinc = sign(end[1] - start[1])
                start[0] += xinc
                start[1] += yinc
            grid[start[1] - minY][start[0] - minX] = "#"
    return grid

# print the grid for debugging purposes
def printGrid(grid):
    for row in grid:
        for space in row:
            print(space, end="")
        print()
    print()


# drop one grain of sand into the grid
def dropGrain(grid, drop_col):
    sand_loc = [drop_col, 0]

    while True:
        # try to move it down
        if grid[sand_loc[1] + 1][sand_loc[0]] == ".":
            sand_loc[1] += 1

        # try to move it down/left
        elif grid[sand_loc[1] + 1][sand_loc[0] - 1] == ".":
            sand_loc[1] += 1
            sand_loc[0] -= 1

        # try to move down/right
        elif grid[sand_loc[1] + 1][sand_loc[0] + 1] == ".":
            sand_loc[1] += 1
            sand_loc[0] += 1

        # else it comes to rest
        else:
            grid[sand_loc[1]][sand_loc[0]] = "O"
            
            # check if it is still in row 0
            if sand_loc[1] == 0:
                return False
            else:
                return True

# run the sand simulation, returning how many steps we got to
def sandSimulation(grid, drop_col):
    steps = 1
    while dropGrain(grid, drop_col):
        steps += 1
        #printGrid(grid)
    return steps

lines = readInput()
minX, maxX, minY, maxY = getBounds(lines)

# add a very long line representing the floor to the input
lines.append([[0, maxY + 2], [1000, maxY + 2]])

# recaluclate new min/max
minX, maxX, minY, maxY = getBounds(lines)

grid = buildGrid(lines, minX, maxX, minY, maxY)
print(sandSimulation(grid, 500 - minX))

