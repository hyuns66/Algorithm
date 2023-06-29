# 기차가 어둠을 헤치고 은하수를~

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

train = []
for _ in range(N):
    train.append(deque([0]*20)) # 0으로 초기화된 20개의 자리

for i in range(M):
    order = list(map(int, sys.stdin.readline().split()))
    if order[0] == 1:
        # order[1]기차의 order[2]번째 좌석에 사람을 태운다.
        train[order[1]-1][order[2]-1] = 1
    elif order[0] == 2:
        # order[1]기차의 order[2]번째 좌석에 사람을 하차시킨다.
        train[order[1]-1][order[2]-1] = 0
    elif order[0] == 3:
        # order[1]기차의 승객들이 모두 한칸씩 뒤로 간다.
        train[order[1]-1].appendleft(0)
        train[order[1] - 1].pop()
    elif order[0] == 4:
        # order[1]기차의 승객들이 모두 한칸씩 앞으로 간다.
        train[order[1] - 1].popleft()
        train[order[1]-1].append(0)

milkyWayTrain = []

for t in train:
    if t not in milkyWayTrain:
        milkyWayTrain.append(t)

print(len(milkyWayTrain))

# deque()를 0으로 초기화하는 방법 = deque([0]*len(my_deque))
