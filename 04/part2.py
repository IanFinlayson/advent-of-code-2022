import sys

def over(a0, a1, b0, b1):
    if a0 <= b0 <= a1:
        return True
    if a0 <= b1 <= a1:
        return True
    return False


def overlaps(a0, a1, b0, b1):
    return over(int(a0), int(a1), int(b0), int(b1))

count = 0
for line in sys.stdin:
    (a0, a1), (b0, b1) = map(lambda p: p.split("-"), line[:-1].split(","))
    print(a0, a1, ",", b0, b1, end=" ")
    if overlaps(a0, a1, b0, b1) or overlaps(b0, b1, a0, a1):
        print("YES!")
        count += 1
    else:
        print("no.")
print(count)


