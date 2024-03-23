import sys

N, H = map(int, sys.stdin.readline().split())
    
top, bottom =  [0 for _ in range(H)], [0 for _ in range(H)]
for i in range(N):
    height = int(sys.stdin.readline()) - 1
    if i & 1 == 0:
        bottom[height] += 1
    else:
        top[height] += 1
        
for i in range(H-2, -1, -1):
    top[i] += top[i+1]
    bottom[i] += bottom[i+1]
       
min_cnt = sys.maxsize
space_cnt = 0
for i in range(H):
    cnt = top[i] + bottom[H-i-1]
    if cnt < min_cnt:
        min_cnt = cnt
        space_cnt = 1
    elif cnt == min_cnt:
        space_cnt += 1
        
print(min_cnt, space_cnt)