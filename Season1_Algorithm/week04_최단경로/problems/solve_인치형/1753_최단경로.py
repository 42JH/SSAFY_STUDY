import sys
import heapq
input = sys.stdin.readline

def bfs(queue):
    heapq.heapify(queue)

    while queue:
        cnt, x = heapq.heappop(queue)

        if check[x] < cnt:
            continue

        for cnt2, nx in arr[x]:
            if check[nx] > cnt + cnt2:
                check[nx] = cnt + cnt2
                heapq.heappush(queue, (cnt + cnt2, nx))

    return


V, E = map(int, input().split())
K = int(input().strip())
arr = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    arr[a].append((c, b))
check = [float('inf')] * (V + 1)
check[K] = 0

bfs([(0, K)])

for i in range(1, V + 1):
    if check[i] != float('inf'):
        print(check[i])
    else:
        print('INF')