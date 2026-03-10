def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left, right)

def merge(left, right):
    global cnt
    if left[-1] > right[-1]:
        cnt += 1

    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result += left[i:]
    result += right[j:]
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_arr = list(map(int, input().split()))
    cnt = 0

    sorted_lst = merge_sort(num_arr)

    print(f'#{tc} {sorted_lst[N//2]} {cnt}')
