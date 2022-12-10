import sys

max = [0, 0, 0]
this = 0

for line in sys.stdin:
    line = line[:-1]
    if line == "":
        if this > max[0]:
            max[0] = this
            max.sort()
        this = 0
    else:
        this += int(line)

print(sum(max))

