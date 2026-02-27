import sys

input = sys.stdin.readline

N, S = map(int, input().split())

A_list = list(map(int, input().split()))
distance_list = []
# 이제 s와 a_list의 각 요소들 사이의 차이(거리)를 계산하면 됩니다!
def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

for i in A_list:
    distance_list.append(abs(S - i))

if len(distance_list) == 1:
    print(distance_list[0])

else:
    gcd = get_gcd(distance_list[0], distance_list[1])

    for d in distance_list:
        value = get_gcd(gcd, d)
        if gcd > value:
            gcd = value
    print(gcd)

