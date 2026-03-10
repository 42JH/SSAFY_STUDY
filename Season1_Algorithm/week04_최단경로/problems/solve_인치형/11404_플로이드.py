import sys
input = sys.stdin.readline
INF = int(1e9)

# 1. 도시의 개수 n, 버스의 개수 m 입력
n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    graph[a][a] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1, n + 1):       # k: 거쳐가는 노드
    for i in range(1, n + 1):   # i: 출발 노드
        for j in range(1, n + 1): # j: 도착 노드
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()