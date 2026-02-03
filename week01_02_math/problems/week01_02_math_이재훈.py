# ============================================
# 베르트랑 공준 - 이재훈
# ============================================

def sieve_of_eratosthenes(limit):
    """에라토스테네스의 체를 이용한 소수 구하기"""
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    
    return is_prime

# 최대값까지의 소수를 미리 구함
MAX_N = 123456
is_prime = sieve_of_eratosthenes(2 * MAX_N)

def bertrand_conjecture():
    """베르트랑 공준: n < p <= 2n 범위의 소수 개수"""
    while True:
        n = int(input())
        if n == 0:
            break
        
        count = 0
        for p in range(n + 1, 2 * n + 1):
            if is_prime[p]:
                count += 1
        
        print(count)

# bertrand_conjecture()


# ============================================
# 골드바흐 파티션 - 이재훈
# ============================================

def goldbach_partition():
    """골드바흐 파티션: 짝수를 두 소수의 합으로 표현하는 방법의 수"""
    # 최대값까지의 소수를 미리 구함
    MAX_N = 1000000
    is_prime = sieve_of_eratosthenes(MAX_N)
    
    t = int(input())
    for _ in range(t):
        n = int(input())
        count = 0
        
        # n/2까지만 확인 (순서만 다른 것은 동일이므로)
        for i in range(2, n // 2 + 1):
            if is_prime[i] and is_prime[n - i]:
                count += 1
        
        print(count)

# goldbach_partition()


# ============================================
# 숨바꼭질 6 - 이재훈
# ============================================

def gcd(a, b):
    """최대공약수 구하기"""
    while b:
        a, b = b, a % b
    return a

def hide_and_seek_6():
    """
    숨바꼭질 6: 모든 동생을 찾기 위한 정수 D의 최댓값
    
    수빈이가 한 번에 ±D만큼 이동 가능할 때,
    모든 동생 위치에 도달 가능한 D의 최댓값을 구한다.
    """
    n, s = map(int, input().split())
    positions = list(map(int, input().split()))
    
    # 각 동생 위치와 수빈이 위치의 차이를 구함
    differences = [abs(pos - s) for pos in positions]
    
    # 모든 차이의 최대공약수가 D의 최댓값
    result = differences[0]
    for diff in differences[1:]:
        result = gcd(result, diff)
    
    print(result)

# hide_and_seek_6()


# ============================================
# 테스트 코드
# ============================================

if __name__ == "__main__":
    print("=== 베르트랑 공준 테스트 ===")
    # 테스트 입력:
    # 1, 10, 13, 100, 1000, 10000, 100000, 0
    # 예상 출력: 1, 4, 3, 21, 135, 1033, 8392
    
    print("\n=== 골드바흐 파티션 테스트 ===")
    # 테스트 입력:
    # 5
    # 6, 8, 10, 12, 100
    # 예상 출력: 1, 1, 2, 1, 6
    
    print("\n=== 숨바꼭질 6 테스트 ===")
    # 테스트 입력 1: 3 3 / 1 7 11 → 2
    # 테스트 입력 2: 3 81 / 33 105 57 → 24
    # 테스트 입력 3: 1 1 / 1000000000 → 999999999
