# 백준 27497번

from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
text = deque()
pop_list = []

for _ in range(N):
    command = input().split()

    if command[0] == '1':
        text.append(command[1])
        pop_list.append('1')

    elif command[0] == '2':
        text.appendleft(command[1])
        pop_list.append('2')

    elif command[0] == '3':
        if text:
            if pop_list[-1] == '1':
                text.pop()
                pop_list.pop()
            elif pop_list[-1] == '2':
                text.popleft()
                pop_list.pop()
        else:
            pass
           
if text:
    print(''.join(text))
else:
    print(0)