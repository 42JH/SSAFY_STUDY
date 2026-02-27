from collections import deque

def solve(board):
  dq = deque()
  dq.append((0,0,1))
  
  visited = [[False]*M for _ in range(N)]
  visited[0][0] = True

  directions = [(1,0),(0,1),(-1,0),(0,-1)]
  
  while dq:
    x, y, dist = dq.popleft()
    if (x,y) == (M-1, N-1):
      return dist
    for dx, dy in directions:
      nx = x + dx
      ny = y + dy
      if 0 <= nx < M and 0 <= ny < N:
        if not visited[ny][nx] and board[ny][nx] == 1:
          dq.append((nx, ny, dist+1))
          visited[ny][nx] = True
  return 0

N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]
result = solve(maze)
print(result)
