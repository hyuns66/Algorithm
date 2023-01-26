# 홀짝 칵테일

import sys

num = list(map(int, sys.stdin.readline().split()))

oddMultiple = 0
evenMultiple = 0
for i in range(3):
    if num[i] % 2 == 0:
        if evenMultiple == 0:
            evenMultiple = num[i]
        else:
            evenMultiple = evenMultiple*num[i]
    else:
        if oddMultiple == 0:
            oddMultiple = num[i]
        else:
            oddMultiple = oddMultiple * num[i]


if oddMultiple != 0:
    print(oddMultiple)
else:
    print(evenMultiple)
