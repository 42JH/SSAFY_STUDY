# 백준 1874번

import sys
input = sys.stdin.readline

n = int(input())

stack = []
command = []
current = 1

flag = True

for _ in range(n):
    target_num = int(input())

    while current <= target_num:
        command.append('+') 
        stack.append(current)
        current += 1

    if target_num == stack[-1]:
        stack.pop()
        command.append('-')
    else:
        flag = False
        break

if flag:
    for i in range(len(command)):
        print(command[i])
else:
    print('NO')