import sys

class Machine:
    def __init__(self, prog):
        self.prog = prog
        self.pc = 0
        self.cycle = 1
        self.reg = 1
        self.latch = None

    def tick(self):
        # print the CRT screen
        xpos = (self.cycle - 1) % 40
        if (self.reg >= xpos - 1) and (self.reg <= xpos + 1):
            print("#", end="")
        else:
            print(".", end="")
        if (self.cycle + 0) % 40 == 0:
            print()
        
        if self.latch != None:
            # latch the result from last time
            self.reg += self.latch
            self.latch = None
        else:
            # fetch a new instruction
            instruction = self.prog[self.pc]
            self.pc += 1
            # execute it
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
while m.cycle <= 240:
    m.tick()

