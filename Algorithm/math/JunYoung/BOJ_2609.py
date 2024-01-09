# 최대공약수와 최소공배수

import sys

A, B = map(int, sys.stdin.readline().split())  # A에 작은 수가 들어간다.
if A > B:
    temp = A
    A = B
    B = temp

divisorA = []

for i in range(1, A + 1):
    if A % i == 0:
        divisorA.append(i)

GCD = divisorA[0]
for j in range(0, len(divisorA)):
    if B % divisorA[j] == 0:
        GCD = divisorA[j]  # 최대 공약수

LCM = sys.maxsize
for i in range(1, B+1):
    if (A * i) % B == 0:
        LCM = A * i
        break  # 최솟값을 찾으면 되므로 바로 break

print(GCD)
print(LCM)
