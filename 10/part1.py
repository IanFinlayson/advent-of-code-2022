import sys

class Machine:
    def __init__(self, prog):
        self.prog = prog
        self.pc = 0
        self.cycle = 1
        self.reg = 1
        self.latch = None

    def tick(self):
        # latch the result from last time
        if self.latch != None:
            self.reg += self.latch
            self.latch = None
        else:
            # fetch
            instruction = self.prog[self.pc]
            self.pc += 1
            
            # execute
            if instruction[0:4] == "noop":
                pass
            else:
                amt = int(instruction[5:])
                self.latch = amt
        self.cycle += 1

# load the program
prog = []
for line in sys.stdin:
    prog.append(line[:-1])
m = Machine(prog)

# step through the cycles we care about
total = 0
while m.cycle <= 220:
    m.tick()
    if m.cycle in [20, 60, 100, 140, 180, 220]:
        total += (m.reg * m.cycle)
print(total)


