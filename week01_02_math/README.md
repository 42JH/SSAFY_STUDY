# 📘 Week 01~02 : 수학 기초

## ✅ 학습 내용
- 최대 공약수(gcd:greatest common divisor, 유클리드호재법사용)
두 수를 모두 나눌 수 있는 가장 큰 수
```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
```
```python
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
```
최소 공배수(LCM - Least common Multiple)
두 수의 공통 배수 중 가장 작은 수
``` python
def lcm(a, b):
    return a * b // gcd(a, b)
```
소수 판별
소수 = 1과 자기 자신만으로 나누어지는 수 
하나의 수
```python
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True 
```
에라토스테네스의 체(여러 소수)
```python
def sieve(n):
    prime = [True] * (n + 1)

    prime[0] = False
    prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False

    return prime
```
골드바흐의 추측
-모든 4 이상의 짝수 n 은 두 소수 p, q의 합으로 표현 가능하다.
= 2보다 큰 모든 짝수는 두 소수의 합으로 표현 가능
```python
MAX = 100000
prime = sieve(MAX)

t = int(input())

for _ in range(t):
    n = int(input())

    l = n // 2
    r = n // 2

    while l >= 2:
        if prime[l] and prime[r]:
            print(l, r)
            break

        l -= 1
        r += 1
```
```python
def goldbach(n):
    prime = sieve(n)
    
    for i in range(2, n//2 + 1):
        if prime[i] and prime[n - i]:
            return i, n - i
```


---

## 📝 문제 목록

| 번호 | 문제 | 유형 | 완료 |
|------|------|------|------|
| #1 : https://www.acmicpc.net/problem/4948 | BOJ 4948 | 베르트라 | ✅ |
| #2 : https://www.acmicpc.net/problem/17103 | BOJ 17103 | 골드바흐 | ✅ |
| #3 : https://www.acmicpc.net/problem/17087 | BOJ 17087 | 숨박꼭질 | ✅ |

---


