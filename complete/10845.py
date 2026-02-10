class Queue:
    def __init__(self):
        self.queue = []

    def push(self,x):
        self.queue.append(x)
    def empty(self):
        return 1 if len(self.queue)==0 else 0
    def pop(self):
        if self.empty():
            return -1
        else:
            temp = self.queue[0]
            self.queue = self.queue[1:]
            return temp
    def size(self):
        return len(self.queue)
    def front(self):
        if self.empty():
            return -1
        else:
            return self.queue[0]
    def back(self):
        if self.empty():
            return -1
        else:
            return self.queue[-1]
import sys
input = sys.stdin.readline

n = (input())
n = n.strip()
n = int(n)
q = Queue()

def queue_command(command):
    if command[0] == "push":
        q.push(command[1])
    elif command[0] == "pop":
        print(q.pop())
    elif command[0] == "size":
        print(q.size())
    elif command[0] == "empty":
        print(q.empty())
    elif command[0] == "front":
        print(q.front())
    elif command[0] == "back":
        print(q.back())

for _ in range(n):
    user = input().split()
    queue_command(user)