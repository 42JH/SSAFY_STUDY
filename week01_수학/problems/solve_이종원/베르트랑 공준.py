import sys
input = sys.stdin.readline

num = 2 * 123456   # 에라토스테네스의 체
prime = [True] * ((2*123456)+1)
prime[1] = False
prime[2] = True
for i in range(2, int(num**0.5) +1):
    for j in range(i*i, num + 1, i):
        prime[j] = False

while True:
    n = int(input().strip())

    if n == 0:
        break

    cnt = 0
    for i in range(n+1, 2*n + 1):
        if prime[i] == True:
            cnt += 1
    print(cnt)