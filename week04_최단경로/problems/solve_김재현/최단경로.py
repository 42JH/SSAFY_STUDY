import heapq
import sys
input = sys.stdin.readline

def dijkstra(start, graph, n):
  INF = int(1e9)
  distance = [INF] * (n+1)
  distance[start] = 0

  pq = []
  heapq.heappush(pq, (0, start))

  while pq:
    dist, now = heapq.heappop(pq)
    if distance[now] < dist:
      continue
    
    for nxt, cost in graph[now]:
      new_cost = dist + cost

      if new_cost < distance[nxt]:
        distance[nxt] = new_cost
        heapq.heappush(pq, (new_cost, nxt))

  return distance

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V+1)]

for _ in range(E):
  u,v,w = map(int, input().split())
  graph[u].append((v,w))

result = dijkstra(K, graph, V)

INF = int(1e9)

for i in range(1, V+1):
  if result[i] == INF:
    print("INF")
  else:
    print(result[i])