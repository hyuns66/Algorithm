# 요세푸스 문제

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

people = deque()
result = []
for i in range(1, N + 1):
    people.append(i)

while len(people) != 0:
    people.rotate(-(K-1))
    result.append(people.popleft())

print("<", end='')
for i in range(0, len(result)):
    if i == len(result) - 1:
        print(str(result[i]) + ">", end='')
    else:
        print(str(result[i]) + ",", end=' ')

"""
    deque의 rotate와
    print의 end를 알게되었다.
"""