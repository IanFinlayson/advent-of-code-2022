import sys

max = 0
this = 0

for line in sys.stdin:
    line = line[:-1]
    if line == "":
        if this > max:
            max = this
        this = 0
    else:
        this += int(line)

print(max)

