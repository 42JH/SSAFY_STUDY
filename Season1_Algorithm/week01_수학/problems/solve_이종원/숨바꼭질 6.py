import sys
input = sys.stdin.readline


N, S = map(int, input().split())

location = list(map(int, input().split()))

gap = []
for i in range(N):  # 수빈의 위치를 기준으로 떨어진 거리를 구한다.
    gap.append(abs(location[i] - S))

def GCD(a, b):  # 최대공약수 구하는 함수 정의
    while b > 0:
        a, b = b, a%b
    return a

answer = gap[0]
for i in range(1, N):
    answer = GCD(answer, gap[i])

print(answer)