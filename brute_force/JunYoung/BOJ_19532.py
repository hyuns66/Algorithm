# 수학은 비대면강의입니다.

import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().split())

y = (c*d-f*a) // (b*d-e*a)
x = (c*e-f*b) // (a*e-d*b)

print(x, y)
