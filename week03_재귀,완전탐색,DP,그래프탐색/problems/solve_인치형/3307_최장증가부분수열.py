# 테스트 케이스 개수 입력
T = int(input())

for t in range(1, T + 1):
    N = int(input())
    # 수열 입력 (공백 기준 분리)
    arr = list(map(int, input().split()))
    
    # 모든 위치에서의 초기 LIS 길이는 1 (자기 자신만 포함할 경우)
    dp = [1] * N
    
    # DP 진행 (O(N^2))
    for i in range(N):
        for j in range(i):
            if arr[j] < arr[i]:
                # 이전 원소(j)가 현재(i)보다 작으면, j까지의 길이에 +1 한 값과 비교
                dp[i] = max(dp[i], dp[j] + 1)
                
    # 결과값 중 가장 큰 값이 전체 수열의 LIS 길이
    print(f"#{t} {max(dp)}")