def dfs(count):
    global max_result
    # 현재 상태(숫자 배열)를 정수로 변환
    current_val = int("".join(cards))
    
    # [가지치기] 이미 해당 교환 횟수에서 이 숫자를 확인했다면 종료
    if (count, current_val) in visited:
        return
    visited.add((count, current_val))

    # 목표 교환 횟수에 도달하면 최대값 갱신
    if count == target_count:
        max_result = max(max_result, current_val)
        return

    # 모든 가능한 두 자리의 조합을 교환 (완전 탐색)
    n = len(cards)
    for i in range(n):
        for j in range(i + 1, n):
            cards[i], cards[j] = cards[j], cards[i]  # 교환
            dfs(count + 1)
            cards[i], cards[j] = cards[j], cards[i]  # 원상복구 (백트래킹)

# 메인 루프 예시
T = int(input())
for t in range(1, T + 1):
    data, target_count = input().split()
    cards = list(data)
    target_count = int(target_count)
    
    max_result = 0
    visited = set()
    dfs(0)
    
    print(f"#{t} {max_result}")