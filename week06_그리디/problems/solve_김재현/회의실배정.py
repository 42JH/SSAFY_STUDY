N = int(input())
time_lst = [tuple(map(int, input().split())) for _ in range(N)]
time_lst = sorted(time_lst, key=lambda x: (x[1], x[0]))

count = 0
current_time = 0
for start, end in time_lst:
    if current_time <= start:
        count += 1
        current_time = end
    
print(count)