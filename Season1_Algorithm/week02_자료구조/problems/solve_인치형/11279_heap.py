import sys
import heapq
input = sys.stdin.readline

queue = []
N = int(input())

for _ in range(N):
    x = int(input())
    if x == 0:
        if queue:
            print(-heapq.heappop(queue))
        else:
            print(0)
    else:
        heapq.heappush(queue, -x)