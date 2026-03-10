from collections import deque

# ==========================================
# [D4] SWEA 1226번: 미로 1 (BFS 탐색)
# ==========================================
def solve_1226():
    """총 10개의 테스트 케이스가 고정으로 주어집니다."""
    print("--- 1226번: 미로 1 실행 ---")
    for _ in range(10):
        tc = int(input())
        maze = [list(input().strip()) for _ in range(16)]
        
        # 1. 출발점(2) 찾기
        sr, sc = -1, -1
        for i in range(16):
            for j in range(16):
                if maze[i][j] == '2':
                    sr, sc = i, j
                    break
            if sr != -1:
                break
                
        # 2. BFS 탐색 초기화
        q = deque([(sr, sc)])
        visited = [[False] * 16 for _ in range(16)]
        visited[sr][sc] = True
        
        dr = [-1, 1, 0, 0] # 상하좌우
        dc = [0, 0, -1, 1]
        
        ans = 0 # 도달 불가능(0)으로 초기화
        
        # 3. BFS 실행
        while q:
            r, c = q.popleft()
            
            # 도착점(3)에 도달한 경우
            if maze[r][c] == '3':
                ans = 1
                break
                
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                
                # 미로 범위 내에 있고, 방문하지 않았으며, 벽(1)이 아닌 경우
                if 0 <= nr < 16 and 0 <= nc < 16 and not visited[nr][nc]:
                    if maze[nr][nc] != '1':
                        visited[nr][nc] = True
                        q.append((nr, nc))
                        
        print(f"#{tc} {ans}")

# ==========================================
# [D3] SWEA 1244번: 최대 상금 (백트래킹 & 메모이제이션)
# ==========================================
def solve_1244():
    """T개의 테스트 케이스가 주어집니다."""
    print("--- 1244번: 최대 상금 실행 ---")
    T = int(input())
    for tc in range(1, T + 1):
        num_str, k_str = input().split()
        nums = list(num_str)
        K = int(k_str)
        
        ans = 0
        visited = set() # (숫자상태, 교환횟수) 중복 탐색 방지
        
        def dfs(count):
            nonlocal ans
            # 교환 횟수를 모두 소진한 경우 최댓값 갱신
            if count == K:
                ans = max(ans, int("".join(nums)))
                return
            
            # 완전 탐색으로 두 위치의 숫자를 교환
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    # 교환
                    nums[i], nums[j] = nums[j], nums[i]
                    
                    state = ("".join(nums), count + 1)
                    if state not in visited:
                        visited.add(state)
                        dfs(count + 1)
                        
                    # 백트래킹 (원상 복구)
                    nums[i], nums[j] = nums[j], nums[i]
                    
        dfs(0)
        print(f"#{tc} {ans}")

# ==========================================
# [D3] SWEA 3307번: 최장 증가 부분 수열 (DP)
# ==========================================
def solve_3307():
    """T개의 테스트 케이스가 주어집니다."""
    print("--- 3307번: 최장 증가 부분 수열 실행 ---")
    T = int(input())
    for tc in range(1, T + 1):
        N = int(input())
        arr = list(map(int, input().split()))
        
        # DP 테이블: dp[i]는 i번째 원소를 마지막으로 하는 LIS 길이 (기본값 1)
        dp = [1] * N
        
        for i in range(1, N):
            for j in range(i):
                # 이전 원소(arr[j])가 현재 원소(arr[i])보다 작으면 증가 수열 성립
                if arr[j] < arr[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    
        print(f"#{tc} {max(dp)}")

# ==========================================
# 실행 부분
# ==========================================
if __name__ == "__main__":
    # solve_1226()
    # solve_1244()
    # solve_3307()
    pass