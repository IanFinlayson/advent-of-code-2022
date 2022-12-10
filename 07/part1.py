import sys

DIR = 0
FILE = 1

class Node:
    def __init__(self, typ, name, size=0):
        self.type = typ
        self.name = name
        self.size = size
        self.children = []
        self.parent = None

    def link(self, child):
        # see if it exists first
        for existing in self.children:
            if existing.name == child.name:
                return existing
        # otherwise add it in
        child.parent = self
        self.children.append(child)
        return child

    def calc_size(self):
        if self.type == DIR:
            for child in self.children:
                self.size += child.calc_size()
        return self.size

    def dump(self, lead=0):
        for i in range(lead):
            print("  ", end="")
        print("-", self.name, end=" ")
        print("({}, size=".format("dir" if self.type == DIR else "file"), self.size, ")", sep="")
        for child in self.children:
            child.dump(lead + 1)

    # this is the actual problem it's asking for -- sum of all dirs <= 100000 in size
    def solve(self):
        total = 0
        if self.type == DIR and self.size <= 100000:
            total += self.size
        for child in self.children:
            total += child.solve()
        return total


def process_input():
    for line in sys.stdin:
        if line[:-1] == "$ cd /":
            # get us kicked off
            root = Node(DIR, "/")
            pwd = root
        elif line[0] == "$" and line[2:4] == "cd":
            dest = line[5:-1]
            if dest == "..":
                pwd = pwd.parent
            else:
                oldpwd = pwd
                pwd = oldpwd.link(Node(DIR, dest))
        elif line[0] == "$" and line[2:4] == "ls":
            # this doesn't really matter
            pass
        else:
            # we are listing files
            a, b = line[:-1].split()
            if a == "dir":
                pwd.link(Node(DIR, b))
            else:
                pwd.link(Node(FILE, b, int(a)))
    return root


root = process_input()
root.calc_size()
root.dump()

print(root.solve())


