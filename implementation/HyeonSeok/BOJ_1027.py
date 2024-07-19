# 기울기가 커지면 보이는 건물 작거나 같으면 안보이는 건물 (오른쪽) 왼쪽이면 그 반대
import sys
from fractions import Fraction
def count_building(idx, direction, buildings):
    pos = idx
    cur_height = buildings[idx]
    count = 0
    grad = sys.maxsize * -direction
    while idx+direction < len(buildings) and idx+direction >= 0:
        new_grad = Fraction((buildings[idx+direction] - cur_height) / (idx+direction-pos))
        if direction==1:
            if new_grad > grad:
                grad = new_grad
                count += 1
        else:
            if new_grad < grad:
                grad = new_grad
                count += 1
        idx += direction
    return count
    
N = int(input())
buildings = list(map(int, input().split()))
answer = 0
for i in range(N):
    right_cnt = count_building(i, 1, buildings)
    left_cnt = count_building(i, -1, buildings)
    answer = max(answer, right_cnt+left_cnt)
print(answer)

