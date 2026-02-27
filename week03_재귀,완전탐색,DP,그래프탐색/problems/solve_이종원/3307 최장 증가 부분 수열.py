T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    table = list(map(int, input().split()))
    dp = [1] * N

    for i in range(1, N):
        for j in range(0, i):
            if table[i] > table[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    max_cnt = max(dp)
    print(f"#{tc} {max_cnt}")