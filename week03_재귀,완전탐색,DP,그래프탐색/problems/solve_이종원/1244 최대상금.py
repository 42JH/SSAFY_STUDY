T = int(input())

def backtracking(num, m):
    global max_money
    if num == k:
        money = [str(i) for i in table]
        cnt = int("".join(money))
        max_money = max(max_money, cnt)
        return

    if m >= a - 2:
        if table.count(max(table)) >= 2:
            backtracking(k, m)
        else:
            table[a - 1], table[a - 2] = table[a - 2], table[a - 1]

            backtracking(num + 1, m)

            table[a - 1], table[a - 2] = table[a - 2], table[a - 1]
    else:
        max_num = max(table[m:])
        if table[m] == max_num:
            backtracking(num, m + 1)

        else:
            for i in range(a - 1, m, -1):
                if table[i] == max_num:
                    table[i], table[m] = table[m], table[i]

                    backtracking(num + 1, m + 1)

                    table[i], table[m] = table[m], table[i]

    return


for tc in range(1, T + 1):
    table, k = input().split()
    k = int(k)
    table = [int(i) for i in table]
    a = len(table)
    max_money = 0

    backtracking(0, 0)

    print(f"#{tc} {max_money}")