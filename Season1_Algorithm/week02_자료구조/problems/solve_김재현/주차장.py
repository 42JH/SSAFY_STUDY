# 백준 5464번

N, M = map(int, input().split())

fee = []
for _ in range(N):
    fee.append(int(input()))

weight = []
for _ in range(M):
    weight.append(int(input()))

queue = []
parking_lot = ['O'] * N
total = 0

for _ in range(2*M):
    car_num = int(input())
    if car_num > 0 and 'O' in parking_lot:
        parking_lot[parking_lot.index('O')] = car_num

    elif car_num > 0 and 'O' not in parking_lot:
        queue.append(car_num)
    
    elif car_num < 0:
        total += weight[abs(car_num) - 1] * fee[parking_lot.index(abs(car_num))]
        parking_lot[parking_lot.index(abs(car_num))] = 'O'
        if queue:
            parking_lot[parking_lot.index('O')] = queue[0]
            queue.pop(0)

print(total)
    



