n = int(input())
m = int(input())

INF = int(1e9)

dist = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
  dist[i][i] = 0

for _ in range(m):
  a, b, c = map(int, input().split())
  dist[a][b] = min(c, dist[a][b])

for k in range(1,n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

for y in range(1, n+1):
  for x in range(1, n+1):
    print(dist[y][x], end=' ')
  print()