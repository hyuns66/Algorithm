# 풍선 터뜨리기
import sys
from collections import deque

N = int(sys.stdin.readline())
moveNum = list(map(int, sys.stdin.readline().split()))

balloon = deque()
for i in range(N):
    balloon.append(i + 1)

pangList = []
while len(balloon) != 0:
    index = balloon.popleft()
    rotateNum = moveNum[index - 1]
    pangList.append(index)
    if rotateNum >= 0:
        balloon.rotate(-(rotateNum - 1))
    else:
        balloon.rotate(-rotateNum)

for i in pangList:
    print(i, end=" ")