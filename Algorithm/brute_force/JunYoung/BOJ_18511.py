# 큰 수 구성하기

import sys
import itertools

N, K = map(int, sys.stdin.readline().split())
KList = list(map(int, sys.stdin.readline().split()))

availList = []
Nlength = len(str(N))

L1 = list(itertools.product(KList, repeat= Nlength))
L2 = []
if Nlength-1 >= 0:
    L2 = list(itertools.product(KList, repeat= Nlength-1))

for i in L1:
    number = int(''.join(str(d) for d in i))
    availList.append(number)
for i in L2:
    number = int(''.join(str(d) for d in i))
    availList.append(number)

availList.sort()
for i in range(len(availList)):
    if availList[i] > N:
        i -= 1
        break

print(availList[i])

# nPr을 하고 싶은데 중복 뽑기를 허용하고 싶으면 product를 쓰면 된다. 뒤에 repeat = 숫자 해줘야하는 거 잊지 말기!
