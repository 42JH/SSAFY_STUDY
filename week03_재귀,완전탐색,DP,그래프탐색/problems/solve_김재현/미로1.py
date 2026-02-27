from collections import deque

def solve(board):
    for j in range(16):
        for i in range(16):
            if board[j][i] == 2:
                start_x = i
                start_y = j
                break
    
    visited = [(start_x, start_y)]
    queue = deque([(start_x, start_y)])
    
    directions = [(1,0),(0,1),(-1,0),(0,-1)]

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < 16 and 0 <= ny < 16:
                if (nx, ny) not in visited and board[ny][nx] == 0:
                    queue.append((nx, ny))
                    visited.append((nx, ny))
                elif (nx, ny) not in visited and board[ny][nx] == 3:
                    return 1
    return 0



T = 10
for _ in range(1, T+1):
    tc = int(input())
    maze = [list(map(int, input().strip())) for _ in range(16)]
    result = solve(maze)
    print(f'#{tc} {result}')