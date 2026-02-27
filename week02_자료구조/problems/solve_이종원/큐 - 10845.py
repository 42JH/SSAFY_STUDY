import sys
from collections import deque
input = sys.stdin.readline

queue = deque()
N = int(input().strip())
for _ in range(N):
    table = list(input().split())
    if table[0] == 'push':
        queue.append(int(table[1]))
    elif table[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif table[0] == 'size':
        print(len(queue))
    elif table[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif table[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    else:
        if queue:
            print(queue[-1])
        else:
            print(-1)