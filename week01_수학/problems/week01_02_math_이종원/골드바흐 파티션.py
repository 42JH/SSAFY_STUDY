import sys
input = sys.stdin.readline

prime = [True] * 1000001  # 에라토스테네스의 체
prime[1] = False
prime[2] = True
for i in range(2, int(1000000**0.5) +1):
    if prime[i] == True:
        for j in range(i*i, 1000001, i):
            prime[j] = False

prime_num = []  # 소수 추출 후 저장
for i in range(2,1000001):
    if prime[i] == True:
        prime_num.append(i)

T = int(input().strip())

for test_case in range(T):
    N = int(input().strip())
    cnt = 0
    for i in prime_num:
        if i > N // 2:  # 순서만 다른 것은 같으므로 절반까지의 수만 확인한다.
            break

        if prime[N-i]: # 뺀 값이 소수에 포암되어 있으면 cnt 1 추가
            cnt += 1

    print(cnt)