from collections import deque

def rotate_gear_one_direction(idx, gears, rotate_dir, gear_dir):
    if gear_dir == 1:
        if idx < 3 and gears[idx][2] != gears[idx+1][6]:
            rotate_gear_one_direction(idx+1, gears, -rotate_dir, 1)
    else:
        if idx > 0 and gears[idx][6] != gears[idx-1][2] :
            rotate_gear_one_direction(idx-1, gears, -rotate_dir, -1)
    gears[idx].rotate(rotate_dir)

gears = list()
for _ in range(4):
    g = deque(list(input()))
    gears.append(g)
    
K = int(input())
test_cases = list()
answer = 0
for _ in range(K):
    test_cases.append(list(map(int, input().split())))

for idx, direction in test_cases:
    idx -= 1
    if idx < 3 and gears[idx][2] != gears[idx+1][6]:
        rotate_gear_one_direction(idx+1, gears, -direction, 1)
    if idx > 0 and gears[idx][6] != gears[idx-1][2]:
        rotate_gear_one_direction(idx-1, gears, -direction, -1)
    gears[idx].rotate(direction)

for idx, g in enumerate(gears):
    if g[0] == '1':
        answer += 2**idx
print(answer)