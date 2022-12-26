import sys

N = int(sys.stdin.readline())
towers = list(map(int, sys.stdin.readline().split()))
answer = list()
towerStack = list()


for i in range(N):
    # 예외적인 케이스 (맨 처음에 스택이 0 상태인 경우)
    if len(towerStack) == 0:        # 스택에 아무것도 없으면 더이상 앞에 큰 타워가 없으니까 0 출력넣고 스택에 본인 넣음
        answer.append(0)
        towerStack.append(i)
        continue
    else:
        # 일반적인 케이스 (수신할 수 있는 타워를 찾는 경우)
        while towers[towerStack[-1]] < towers[i]:   # 스택 내에서 수신가능한 타워를 찾는 과정
            towerStack.pop()
            if len(towerStack) == 0:                # 탐색중 스택이 비어버린 경우 (수신 가능한 타워가 없음)
                answer.append(0)
                towerStack.append(i)
                break
    if towerStack[-1] == i:                         # while문 break로 빠져나오고 continue 바로 하기 위한 조건문
        continue
    answer.append(towerStack[-1] + 1)               # 수신가능한 타워를 while문에서 정상적으로 찾은 경우 정답 출력
    towerStack.append(i)

print(*answer)
