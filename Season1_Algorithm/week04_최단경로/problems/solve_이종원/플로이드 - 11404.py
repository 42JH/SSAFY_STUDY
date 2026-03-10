import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    check = [float('inf')] * (N + 1)
    check[start] = 0

    while queue:
        cnt, x = heapq.heappop(queue)

        if check[x] < cnt:
            continue

        for cnt2, nx in table[x]:
            if check[nx] > cnt + cnt2:
                check[nx] = cnt + cnt2
                heapq.heappush(queue, (cnt + cnt2, nx))

    for i in range(1, N + 1):
        if check[i] != float('inf'):
            print(check[i], end=" ")
        else:
            print(0, end=" ")
    print()


N = int(input().strip())
M = int(input().strip())
table = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    table[a].append((c, b))

for i in range(1, N + 1):
    dijkstra(i)