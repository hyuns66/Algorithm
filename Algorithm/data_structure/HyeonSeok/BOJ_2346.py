import sys
from collections import deque

N = int(sys.stdin.readline())

scale = list(sys.stdin.readline().split()) # balloons 를 탐색하면서 balloons의 인덱스로 scale 참조해서 이동
balloons = deque()  # 실제로 회전시킬 풍선들

for i in range(N):
    balloons.append(i+1)    # 각 풍선에 인덱스를 지정해주어서 scale을 참조해올 수 있도록 함

while balloons:
    n = balloons.popleft()  # 풍선이 모두 사라질 때  까지 하나씩 pop
    move = int(scale[n-1])  # 이동해야 할 크기
    if move > 0:       # 오른쪽으로 이동 -> 덱을 왼쪽으로 회전 (오른쪽의 값을 맨 앞으로 가져온 후 popleft 하기 위함)
        balloons.rotate(-int(scale[n-1])+1)     # popleft가 위에서 실행되면서 오른쪽으로 이미 한칸 이동한 효과 상쇄 하기 위해 +1
    else:               # 왼쪽으로 이동 -> 덱을 오른쪽으로 회전 (왼쪽의 값을 맨 앞으로 가져온 후 popleft)
        balloons.rotate(-int(scale[n-1]))       # popleft는 왼쪽으로 회전되는 수에 영향을 미치지 않기 때문에 그대로 사용.
    if not balloons:
        print(n, end='')        # 굳이 리스트에 담고 for문을 한번 더 돌리면 메모리와 시간이 낭비되기 때문에
    else:                       # 적절히 출력형식에 맞게 바로바로 출력하도록 구현
        print(str(n)+" ", end='')