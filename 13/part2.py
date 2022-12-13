import sys
from functools import cmp_to_key

def isOrdered(left, right):
    # if they are both lists
    if isinstance(left, list) and isinstance(right, list):
        # if one runs out first, that tells us the order
        if len(left) == 0 and len(right) == 0:
            return 0
        elif len(left) == 0:
            return -1
        elif len(right) == 0:
            return 1
        
        # if out of order, we know the order
        result = isOrdered(left[0], right[0]) 
        if result == -1:
            return -1
        elif result == 1:
            return 1
        else:
            # move to next
            return isOrdered(left[1:], right[1:])
    
    # if only one is a list, make the other one a list too
    elif isinstance(left, list):
        return isOrdered(left, [right])
    elif isinstance(right, list):
        return isOrdered([left], right)

    # else they are both just numbers
    else:
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            # no result, so move on to next thing
            return 0

lines = sys.stdin.readlines()
packets = []
packets.append([[2]])
packets.append([[6]])

for i in range(0, len(lines), 3):
    # parsing this WAY easier in python
    packets.append(eval(lines[i]))
    packets.append(eval(lines[i + 1]))
   
packets.sort(key = cmp_to_key(isOrdered))
index = 1
for p in packets:
    if p == [[2]]:
        a = index
    elif p == [[6]]:
        b = index
    index += 1
print(a * b)
