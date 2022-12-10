import sys

def split(line):
    middle = len(line) // 2
    return line[:middle], line[middle:]

def common(line1, line2, line3):
    for letter in line1:
        if (letter in line2) and (letter in line3):
            return letter
    return None

def points(letter):
    code = ord(letter)
    if code >= 97:
        return code - 96
    else:
        return code - 38

total = 0
line1 = ""
line2 = ""
elfno = 1
for line in sys.stdin:
    if elfno == 1:
        line1 = line
        elfno += 1
    elif elfno == 2:
        line2 = line
        elfno += 1
    else:
        letter = common(line1, line2, line)
        total += points(letter)
        elfno = 1
    
print(total)
    
