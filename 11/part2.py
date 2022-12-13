import sys

# for part two, we limit the sizes of the numbers by modding them by the product
# of all the divisibility tests.  This doesn't change the answer since modulus
# is associative in a way: (X + Y) % Z is the same as ((X % Z) + (Y % Z) % Z)
# I had to spend some time mucking around with this before I understood why it works...
# the divisorProducts is the LCM of the numbers (which are all prime)
divisorProducts = 1

class Monkey:
    def __init__(self, items, modfunc, divisor, t_recip, f_recip):
        self.items = items
        self.modfunc = modfunc
        self.divisor = divisor
        self.t_recip = t_recip
        self.f_recip = f_recip
        self.inspected = 0

    def turn(self, compatriots):
        while len(self.items) > 0:
            # take out our next item
            item = self.items.pop(0)
            
            # handle the item, DONT divide by 3
            item = self.modfunc(item)
            
            # instead mod it by the product of all divisors
            # this keeps numbers smaller while retaining correct answer
            item = item % divisorProducts
            
            # do the test
            if item % self.divisor == 0:
                recip = self.t_recip
            else:
                recip = self.f_recip

            # send to other monkey
            compatriots[recip].items.append(item)
            
            # mark it
            self.inspected += 1

# read in the data this is very hackish feeling
def getMonkeys():
    global divisorProducts
    lines = sys.stdin.readlines()
    monkey_count = len(lines) + 1 // 7
    monkeys = []
    for pointer in range(0, len(lines), 7):
        # grab starting items
        items = list(map(int, lines[pointer + 1][18:-1].split(", ")))
        
        # get the modification function
        operator = lines[pointer + 2][23]
        operand = lines[pointer + 2][25:-1]
        if operand == "old":
            if operator == "+":
                modfunc = lambda x: x + x
            else:
                modfunc = lambda x: x * x
        else:
            # the way python does scope is extremely annoying >:(
            if operator == "+":
                modfunc = lambda x, o=operand: x + int(o)
            else:
                modfunc = lambda x, o=operand: x * int(o)
        
        # grab the divisor and recipients
        divisor = int(lines[pointer + 3][21:-1])
        t_recip = int(lines[pointer + 4][29:-1])
        f_recip = int(lines[pointer + 5][30:-1])
       
        # times the divisor into its product so we can mod by it
        divisorProducts *= divisor
        
        monkeys.append(Monkey(items, modfunc, divisor, t_recip, f_recip))
    return monkeys

def round(monkeys):
    for monkey in monkeys:
        monkey.turn(monkeys)
        #print("Monkey inspected", monkey.inspected, "items")

monkeys = getMonkeys()
for i in range(10000):
    round(monkeys)

maxes = [0, 0]
for monkey in monkeys:
    maxes.append(monkey.inspected)
    maxes.sort(reverse = True)
    maxes = maxes[:-1]

print(maxes[0] * maxes[1])

