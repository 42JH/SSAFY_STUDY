from collections import deque
T = 10

def bfs(a, b):
    queue = deque([(a, b)])
    check = [[0] * 16 for _ in range(16)]
    check[a][b] = 1
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

    while queue:
        x, y = queue.popleft()
        if x == e_x and y == e_y:
            print(f"#{tc} 1")
            break

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if 0 <= nx < 16 and 0 <= ny < 16:
                if table[nx][ny] != '1' and not check[nx][ny]:
                    check[nx][ny] = 1
                    queue.append((nx, ny))
    else:
        print(f"#{tc} 0")

for test_case in range(1, T + 1):
    tc = int(input())
    table = [list(input()) for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if table[i][j] == '2':
                s_x, s_y = i, j
            elif table[i][j] == '3':
                e_x, e_y = i, j

    bfs(s_x, s_y)