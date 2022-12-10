import sys

def split(line):
    middle = len(line) // 2
    return line[:middle], line[middle:]

def common(a, b):
    for letter in a:
        if letter in b:
            return letter
    return None

def points(letter):
    code = ord(letter)
    if code >= 97:
        return code - 96
    else:
        return code - 38

total = 0
for line in sys.stdin:
    first, second = split(line[:-1])
    letter = common(first, second)
    total += points(letter)
    
print(total)
    
