# 에라토스테네스의 체(여러 소수)
def sieve(n):
    prime = [True] * (n + 1)

    prime[0] = False
    prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False

    prime_numbers = []
    for num in range(n + 1):
        if prime[num]:
            prime_numbers.append(num)
    return prime_numbers

while True:
    N = int(input())
    if N == 1:
        print(1)
    elif N == 0:
        break
    else:
        difference = list(set(sieve(2 * N)) - set(sieve(N)))
        print(len(difference))
