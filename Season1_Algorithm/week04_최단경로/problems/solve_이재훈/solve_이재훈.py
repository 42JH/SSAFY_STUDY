import sys
import heapq
from collections import deque

# ==========================================
# [Silver I] 백준 2178번: 미로 탐색 (BFS)
# ==========================================
def solve_2178():
    """가중치가 없는 그래프의 최단 경로는 BFS를 사용합니다."""
    print("--- 2178번: 미로 탐색 실행 ---")
    input = sys.stdin.readline
    N, M = map(int, input().split())
    
    # 공백 없이 붙어서 입력되므로 문자열을 한 글자씩 잘라 정수로 변환
    maze = [list(map(int, list(input().strip()))) for _ in range(N)]
    
    # 방향 벡터 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque([(0, 0)])
    
    while q:
        x, y = q.popleft()
        
        # 목적지에 도달하면 누적된 거리 출력 후 종료
        if x == N - 1 and y == M - 1:
            print(maze[x][y])
            return
            
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # 미로 범위 내에 있고, 이동할 수 있는 칸(1)인 경우
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1:
                # 방문 처리와 동시에 거리를 누적
                maze[nx][ny] = maze[x][y] + 1
                q.append((nx, ny))



# ==========================================
# [Gold IV] 백준 1753번: 최단경로 (다익스트라)
# ==========================================
def solve_1753():
    """특정 시작점에서 다른 모든 정점까지의 최단 경로를 구합니다."""
    print("--- 1753번: 최단경로 실행 ---")
    input = sys.stdin.readline
    V, E = map(int, input().split())
    K = int(input())
    
    # 인접 리스트 생성
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        
    INF = int(1e9) # 무한대 설정
    dist = [INF] * (V + 1)
    dist[K] = 0 # 시작점의 거리는 0
    
    # 우선순위 큐 (거리, 노드번호)
    q = [(0, K)]
    
    while q:
        d, now = heapq.heappop(q)
        
        # 이미 처리된 적 있는 노드라면 무시 (더 짧은 경로가 이미 존재)
        if dist[now] < d:
            continue
            
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for next_node, weight in graph[now]:
            cost = d + weight
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < dist[next_node]:
                dist[next_node] = cost
                heapq.heappush(q, (cost, next_node))
                
    # 결과 출력
    for i in range(1, V + 1):
        if dist[i] == INF:
            print("INF")
        else:
            print(dist[i])

# ==========================================
# [Gold IV] 백준 11404번: 플로이드 (플로이드-워셜)
# ==========================================
def solve_11404():
    """모든 지점에서 다른 모든 지점까지의 최단 경로를 구합니다."""
    print("--- 11404번: 플로이드 실행 ---")
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    
    INF = int(1e9)
    # 2차원 거리 배열 초기화
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    
    # 자기 자신으로 가는 비용은 0으로 초기화
    for i in range(1, n + 1):
        dist[i][i] = 0
        
    # 간선 정보 입력
    for _ in range(m):
        a, b, c = map(int, input().split())
        # 동일한 노선이 여러 개일 수 있으므로 가장 짧은 거리만 저장
        dist[a][b] = min(dist[a][b], c)
        
    # 플로이드-워셜 알고리즘 수행 (k: 거쳐가는 노드)
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                
    # 결과 출력
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            if dist[i][j] == INF:
                row.append(0)
            else:
                row.append(dist[i][j])
        print(*row)



# ==========================================
# 실행 부분
# ==========================================
if __name__ == "__main__":
    # solve_2178()
    # solve_1753()
    # solve_11404()
    pass