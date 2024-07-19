# 귀여운 라이언
import sys

N, K = map(int, sys.stdin.readline().split())
cuties = list(map(int, sys.stdin.readline().split()))

shortest_size = sys.maxsize
ryan_count = 1 if cuties[0] == 1 else 0

start_idx = 0
end_idx = 0

while True:
    if ryan_count >= K:
        if end_idx - start_idx < shortest_size:
            shortest_size = end_idx - start_idx + 1

        # 시작 포인터 줄여나가기
        if cuties[start_idx] == 1:
            ryan_count -= 1
        start_idx += 1
    elif end_idx+1 < N:
        end_idx += 1
        if cuties[end_idx] == 1:
            ryan_count += 1
    else:
        break

if shortest_size == sys.maxsize:
    shortest_size = -1

print(shortest_size)
