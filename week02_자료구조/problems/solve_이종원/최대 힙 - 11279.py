import sys
import heapq
input = sys.stdin.readline

queue = []
N = int(input().strip())
for _ in range(N):
    a = int(input().strip())
    if a == 0:
        if queue:
            print(-heapq.heappop(queue))
        else:
            print(0)
    else:
        heapq.heappush(queue, -a)