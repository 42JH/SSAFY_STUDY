# 먼저 1로 표현된 섬을 2,3,4... 로 라벨링
# 이후 섬의 어느 한 점에서 특정 방향으로 전진했을때 0(바다)라면 그 점과 방향을 함수에 넣음
# 그 점에서 지정한 방향으로 전진했을때 지도 범위 밖으로 벗어나거나, 다른 섬에 도착했으나 다리 길이가 1이면 return, 0(바다)인 경우 길이 1 추가하고 continue
# 다리 길이가 2 이상인 상태에서 다른 섬에 도착한 경우 출발한 섬의 번호와 도착한 섬의 번호를 정렬후, 이 번호들을 튜플로 묶어 딕셔너리의 key로, 다리길이를 value로 저장
# 이때 같은 key값에서 value가 더 작은 경우 그 값으로 갱신
# 모든 다리의 정보가 기록되면 이 정보들을 꺼내 다리 길이, (섬번호1, 섬번호2) 순으로 다시 튜플로 묶은 뒤 빈 리스트에 추가
# 이 리스트를 정렬하면 다리 길이 기준으로 오름차순으로 정렬됨
# 이 리스트에서 다리 길이, 섬 번호들을 꺼내어 크루스칼 알고리즘 실행하여 최종적으로 만들 다리 선택
# 만들어진 다리가 (섬의 개수 -1) 과 같으면 다리 길이의 합 출력, 아닌 경우 -1 출력


from collections import deque

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(start, num):
    queue = deque([start])

    while queue:
        start_x, start_y = queue.popleft()
        for dx, dy in directions:
            nx = start_x + dx
            ny = start_y + dy
            if 0 <= nx < M and 0 <= ny < N and board[ny][nx] == 1:
                board[ny][nx] = num
                queue.append((nx, ny))
    
    return

def make_bridge(start, direction, island_num):
    bridge_x, bridge_y = start
    dir_x, dir_y = direction
    length = 0
    
    while True:
        bridge_x += dir_x
        bridge_y += dir_y

        if not (0 <= bridge_x < M and 0 <= bridge_y < N):
            return
        
        if board[bridge_y][bridge_x] == island_num:
            return
        if board[bridge_y][bridge_x] == 0:
            length += 1
            continue
        if board[bridge_y][bridge_x] != island_num and length >= 2:
            a, b = sorted((island_num, board[bridge_y][bridge_x]))
            if (a,b) not in bridge or bridge[(a,b)] > length:
                bridge[(a,b)] = length
        return

def find_parent(parent, node):
    if parent[node] != node:
        parent[node] = find_parent(parent, parent[node])
    return parent[node]

def union_parent(parent, node1, node2):
    a = find_parent(parent, node1)
    b = find_parent(parent, node2)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

idx = 2
for y in range(N):
    for x in range(M):
        if board[y][x] == 1:
            board[y][x] = idx
            bfs((x, y), idx)
            idx += 1

bridge = dict()

for y in range(N):
    for x in range(M):
        if board[y][x] != 0:
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < M and 0 <= ny < N and board[ny][nx] == 0:
                    make_bridge((x, y), (dx, dy), board[y][x])

edges = []
for (a, b), l in bridge.items():
    edges.append((l,a,b))

edges.sort()
result = 0
bridge_count = 0

parent = [0] * idx

for i in range(2, idx):
    parent[i] = i

for edge in edges:
    l, i1, i2 = edge
    if find_parent(parent, i1) != find_parent(parent, i2):
        union_parent(parent, i1, i2)
        result += l
        bridge_count += 1

island_count = idx -2

if bridge_count == island_count - 1:
    print(result)
else:
    print(-1)