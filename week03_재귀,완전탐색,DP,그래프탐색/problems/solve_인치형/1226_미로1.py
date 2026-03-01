from collections import deque

def bfs(num1, num2):
    visited = [[0] * N for _ in range(N)]
    visited[num1][num2] = 1
    queue = deque([(num1, num2)])


    while queue:
        cr, cc = queue.popleft()
        if maze[cr][cc] == 3:
            return 1
        
        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]

        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]

            if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != 1 and not visited[nr][nc]:
                visited[nr][nc] = 1
                queue.append((nr, nc))
    return 0

    
T = 10
for _ in range(T):
    tc = int(input())
    N = 16              # 미로의 크기: N * N
    maze = [list(map(int, input().strip())) for _ in range(N)]

    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sr, sc = i, j
    # 도착점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 3:
                er, ec = i, j
    
    print(f"#{tc} {bfs(sr, sc)}")

    