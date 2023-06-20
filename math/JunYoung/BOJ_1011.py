# 26    
# 2+6=8 => 68
# 6+8=14 => 84
# 8+4=12 => 42
# 4+2=6 => 26
# 이게 왜 돌아오지? 신기하네

import sys

N = int(sys.stdin.readline())
cycleCount = 0

if len(str(N)) == 1:
    N = int(str(N).zfill(2))
# 앞에 0 안달아줘도 잘 되는것 같은디?

newNum = N
while True:
    temp = newNum // 10 + newNum % 10
    newNum = (newNum % 10) * 10 + temp % 10
    cycleCount += 1
    if newNum == N:
        print(cycleCount)
        break
