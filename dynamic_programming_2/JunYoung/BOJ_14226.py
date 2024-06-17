# 이모티콘
# 1. 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
# 2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
# 3. 화면에 있는 이모티콘 중 하나를 삭제한다.

# 이미 화면에 이모티콘 1개를 입력했다. 영선이가 S개의 이모티콘을 화면에 만드는데 걸리는 시간의 최솟값??
# S (2 ≤ S ≤ 1000)

import sys
from collections import deque

S = int(sys.stdin.readline())
q = deque()
q.append((1,0)) #(현재 이모티콘 수, 클립보드에 복사된 이모티콘 수)

visited = dict()
visited[(1, 0)] = 0

while q:
    current, clip_board = q.popleft()
    sec = visited[(current, clip_board)]
    if current == S:
        print(visited[(current, clip_board)])
        break

    # 1. 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
    if (current, current) not in visited:
        visited[(current, current)] = sec + 1
        q.append((current,current))
    # 2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
    if (current+clip_board, clip_board) not in visited:
        visited[(current+clip_board, clip_board)] = sec + 1
        q.append((current+clip_board, clip_board))
    # 3. 화면에 있는 이모티콘 중 하나를 삭제한다.
    if (current-1, clip_board) not in visited:
        visited[(current-1, clip_board)] = sec + 1
        q.append((current-1, clip_board))

# visited 있으면 안가는 이유는, 같은 게 이미 visited 있다면 그 경우와 같은 결과인데, 오히려 시간만 늘어나게 되므로 가지 않는다!

# 답지 보고 품!