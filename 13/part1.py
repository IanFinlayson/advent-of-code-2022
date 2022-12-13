import sys


def isOrdered(left, right):
    # if they are both lists
    if isinstance(left, list) and isinstance(right, list):
        # if one runs out first, that tells us the order
        if len(left) == 0:
            return True
        elif len(right) == 0:
            return False
        
        # if out of order, we know the order
        result = isOrdered(left[0], right[0]) 
        if result == True:
            return True
        elif result == False:
            return False
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
            return True
        elif left > right:
            return False
        else:
            # no result, so move on to next thing
            return None



lines = sys.stdin.readlines()
index = 1
total = 0
for i in range(0, len(lines), 3):
    # parsing this WAY easier in python
    left = eval(lines[i])
    right = eval(lines[i + 1])
    
    # check it
    order = isOrdered(left, right)
    if order == None:
        print("hmmm...")
    if order == True:
        total += index
    index += 1
    
print(total)

