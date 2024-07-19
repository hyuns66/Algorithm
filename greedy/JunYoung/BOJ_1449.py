# 수리공 항승
# 항승이는 길이가 L인 테이프를 무한개 가지고 있다.
# 물을 막을 때, 적어도 그 위치의 좌우 0.5만큼 간격을 줘야함

# 항승이가 필요한 테이프의 최소 개수를 구하는 프로그램
import sys

N, L = map(int, sys.stdin.readline().split())
leak_spot = list(map(int, sys.stdin.readline().split()))
leak_spot.sort()

tape_end = 0
count = 0
for i in leak_spot:
    if i + 0.5 > tape_end: # 해당 물 구멍을 막지못하면
        count += 1
        tape_end = max(tape_end, i - 0.5) + L # 현재 tape_end랑 구멍 -0.5중 큰거부터 L만큼 붙이기
        #print(f"구멍 {i} 새롭게 테이프 처리")
        #print(f"tape_end =  {tape_end}")

print(count)

