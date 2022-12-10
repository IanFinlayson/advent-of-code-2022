import sys

def contains(a0, a1, b0, b1):
    return int(b0) >= int(a0) and int(b1) <= int(a1)

count = 0
for line in sys.stdin:
    (a0, a1), (b0, b1) = map(lambda p: p.split("-"), line[:-1].split(","))
    if contains(a0, a1, b0, b1) or contains(b0, b1, a0, a1):
        count += 1
print(count)


