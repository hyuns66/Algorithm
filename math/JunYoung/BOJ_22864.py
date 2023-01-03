# 피로도

import sys

userInput = sys.stdin.readline().split()
A = int(userInput[0])  # 피로도
B = int(userInput[1])  # 처리할 수 있는 일
C = int(userInput[2])  # 휴식으로 감소하는 피로도
M = int(userInput[3])  # 피로도 한계선

# 하루에 번 아웃이 되지 않도록 일을 할 때 최대 얼마나 많은 일을 할 수 있는지 출력한다.

totalStress = 0
totalWork = 0
for i in range(0, 24):
    if totalStress + A <= M:  # 번아웃이 안온다면
        totalStress += A
        totalWork += B
    else:  # 번아웃이 온다면
        totalStress -= C
        if totalStress < 0:
            totalStress = 0  # 피로도는 음수로 내려갈 수 없다.
    # print(str(i+1)+":"+str(totalStress)+":"+str(totalWork))

print(totalWork)

# 틀린이유: M 이하이면 번아웃 안오는데, M 미만이어야 번아웃 안오는 줄 착각함.
