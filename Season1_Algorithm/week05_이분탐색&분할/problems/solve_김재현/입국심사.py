T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    counter = [int(input()) for _ in range(N)]

    low = 1
    high = max(counter) * M
    answer = float('inf')
    
    while low <= high:
        time = (high + low) // 2
        sum_people = 0
        for t in counter:
            sum_people += time // t
            if sum_people >= M:
                break
        if sum_people >= M:
            answer = min(answer, time)
            high = time - 1
        else:
            low = time + 1
    
    print(f'#{tc} {int(answer)}')