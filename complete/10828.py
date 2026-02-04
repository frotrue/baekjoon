class Stack:
    def __init__(self):
        self.arr = []

    def push(self, value):
        self.arr.append(value)
    def pop(self):
        if self.empty():
            return -1
        else:
            return self.arr.pop()
    def size(self):
        return len(self.arr)
    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0
    def top(self):
        if self.empty():
            return -1
        else:
            return self.arr[-1]

import sys

stack = Stack()
n =  int(sys.stdin.readline())
for _ in range(n):
    command = sys.stdin.readline().strip().split()
    if command[0] == "push":
        stack.push(int(command[1]))
    elif command[0] == "pop":
        print(stack.pop())
    elif command[0] == "size":
        print(stack.size())
    elif command[0] == "empty":
        print(stack.empty())
    elif command[0] == "top":
        print(stack.top())