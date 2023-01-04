#최소 공배수

import sys

t = int(sys.stdin.readline())
result = []


def lcm(a, b):
    if a > b:
        temp = a
        a = b
        b = temp

    for k in range(1, b + 1):
        if ((a * k) >= b) & (((a * k) % b) == 0):
            return a * k


for i in range(0, t):
    A, B = map(int, sys.stdin.readline().split())
    result.append(lcm(A, B))

for i in range(0, t):
    print(result[i])

"""
math.lcm 쓰려 했는데
lcm은 파이썬3.9버전부터 사용할 수 있는데
파이썬 3.5~3.8 버전에서는 없다고 뜬다.
"""