# 백준 10828번

import sys
input = sys.stdin.readline

N = int(input())
data_list = []

for _ in range(N):
    command = input().split()
    if command[0] == 'push':
        data_list.append(int(command[1]))

    elif command[0] == 'pop':
        if data_list:
            print(data_list.pop())
        else:
            print(-1)

    elif command[0] == 'size':
        print(len(data_list))

    elif command[0] == 'empty':
        if not data_list:
            print(1)
        else:
            print(0)
            
    elif command[0] == 'top':
        if data_list:
            print(data_list[-1])
        else:
            print(-1)