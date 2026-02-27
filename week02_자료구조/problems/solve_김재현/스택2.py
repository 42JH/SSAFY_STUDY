# 백준 28278번

import sys
input = sys.stdin.readline

data_list = []
N = int(input())
for _ in range(N):
    command = list(map(int, input().split()))
    if command[0] == 1:
        data_list.append(int(command[1]))

    elif command[0] == 2:
        if data_list:
            print(data_list.pop())
        else:
            print(-1)

    elif command[0] == 3:
        print(len(data_list))

    elif command[0] == 4:
        if not data_list:
            print(1)
        else:
            print(0)
            
    elif command[0] == 5:
        if data_list:
            print(data_list[-1])
        else:
            print(-1)