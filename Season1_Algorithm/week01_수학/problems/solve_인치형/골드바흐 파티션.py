import sys
input = sys.stdin.readline

prime = [True] * 1000001  
prime[1] = False
prime[2] = True
for i in range(2, int(1000000**0.5) +1):
    if prime[i] == True:
        for j in range(i*i, 1000001, i):
            prime[j] = False

prime_list = []
for i in range(2, 1000001):
    if prime[i] == True:
        prime_list.append(i)
    
T = int(input().strip())

for tc in range(T):
    N = int(input().strip())
    count = 0
    for i in prime_list:
        if i > N //2:        
            break
        
        if prime[N - i]:     # 이 부분 이해가 잘 안됨
            count += 1
    
    print(count)