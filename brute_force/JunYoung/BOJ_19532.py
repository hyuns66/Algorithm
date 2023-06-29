# 수학은 비대면강의입니다.

import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().split())

y = (c*d-f*a) // (b*d-e*a)
x = (c*e-f*b) // (a*e-d*b)

print(x, y)

#divide by zero 에러 => a가 0일 수도 있기 때문 분모에 a만 있던 식에선 a가 0이 되면 안된다. 따라서 현재 식으로 수정함.