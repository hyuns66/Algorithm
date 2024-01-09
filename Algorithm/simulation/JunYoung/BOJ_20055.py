# 컨베이어 벨트 위의 로봇
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
container_belt = deque()
robot = deque(0 for i in range(2*N))

durability = list(map(int, sys.stdin.readline().split()))

for i in durability:
    container_belt.append(i)

count = 0
level = 1
answer = 1 # 문제에서 말하는 단계
while count < K:
    if level == 1:
        container_belt.rotate(1)
        robot.rotate(1)
        robot[N-1] = 0 # 내리는 칸 비우기
        level = 2
    elif level == 2:
        for i in range(N-1): # 0~N-2까지의 칸 탐색 # N-1은 내리는 칸이라 볼 필요 x
            if robot[N-2-i] == 1 and robot[N-2-i+1] == 0: #로봇이 있을 때 다음칸에 로봇이 없고,
                if container_belt[N-2-i+1] > 0: # 한칸 다음이 내구도가 1 이상이면
                    robot[N-2-i] = 0
                    robot[N-2-i+1] = 1 # 로봇 한칸 이동
                    if (N-2-i+1) == N-1:
                        robot[N-2-i+1] = 0 # 내리는 칸 비우기
                    container_belt[N-2-i+1] -= 1 # 내구도 감소
                    if container_belt[N-2-i+1] == 0:
                        count += 1
        level = 3
    elif level == 3:
        if container_belt[0] > 0:
            container_belt[0] -= 1 # 내구도 감소
            robot[0] = 1 # 로봇 올려놓기
            if container_belt[0] == 0:
                count+=1
        level = 4
    elif level == 4:
        if count >= K:
            break
        else:
            level = 1
            answer += 1

print(answer)


# 40분 소요
