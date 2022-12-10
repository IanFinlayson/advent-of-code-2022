
line = input()

def multiple(window):
    for i in range(4):
        for j in range(i + 1, 4):
            if window[i] == window[j]:
                return True
    return False

for i in range(4, len(line)):
    window = line[i-4:i]
    print("Testing", window)
    if not multiple(window):
        print("Found!")
        print(i)
        break


