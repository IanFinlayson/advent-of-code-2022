line = input()

def multiple(window):
    for i in range(14):
        for j in range(i + 1, 14):
            if window[i] == window[j]:
                return True
    return False

for i in range(14, len(line)):
    window = line[i-14:i]
    if not multiple(window):
        print(i)
        break


