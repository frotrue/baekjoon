class Sets:
    def __init__(self):
        self.sets = []
    def add(self, x):
        if not self.check(x):
            self.sets.append(x)
    def remove(self,x):
        if self.check(x):
            self.sets.remove(x)
    def check(self,x):
        return 1 if x in self.sets else 0
    def toggle(self,x):
        if self.check(x):
            self.remove(x)
        else:
            self.sets.append(x)
    def all(self):
        self.sets = [i for i in range(1,21)]
    def empty(self):
        self.sets = []
    def command(self, com):
        if com[0] =="add":
            self.add(int(com[1]))
        elif com[0] =="remove":
            self.remove(int(com[1]))
        elif com[0] =="check":
            print(self.check(int(com[1])))
        elif com[0] =="toggle":
            self.toggle(int(com[1]))
        elif com[0] =="all":
            self.all()
        elif com[0] =="empty":
            self.empty()
import sys
input = sys.stdin.readline
n = int(input())
s = Sets()
for _ in range(n):
    com = input().split()
    s.command(com)