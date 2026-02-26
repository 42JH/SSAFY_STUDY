def dfs(i):
    if memo[i] != -1:
        return memo[i]
    
    result = 1
    for j in range(i+1, N):
        if arr[j] > arr[i]:
            result = max(result, dfs(j)+1)
    memo[i] = result
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    memo = [-1] * N
    ans = 0
    for i in range(N):
        ans = max(ans, dfs(i))
    
    print(f'#{tc} {ans}')