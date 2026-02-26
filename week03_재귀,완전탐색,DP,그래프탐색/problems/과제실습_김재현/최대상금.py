def dfs(depth):
    global answer

    temp = ''.join(map(str, num_arr))
    if (temp, depth) in visited:
        return

    visited.add((temp, depth))

    if depth == n:
        answer = max(answer, int(temp))
        return

    length = len(num_arr)
    for i in range(length):
        for j in range(i+1, length):
            num_arr[i], num_arr[j] = num_arr[j], num_arr[i]
            dfs(depth + 1)
            num_arr[i], num_arr[j] = num_arr[j], num_arr[i]
    

T = int(input())
for tc in range(1, T+1):
    num, n = map(int, input().split())
    num_arr = list(str(num))

    visited = set()

    answer = 0

    dfs(0)
    print(f'#{tc} {answer}')