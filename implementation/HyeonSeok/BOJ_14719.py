import sys

H, W = map(int, sys.stdin.readline().split())
graph = list(map(int, sys.stdin.readline().split()))
answer = 0

for y in range(0, H+1):
    temp = 0
    cnt = 0
    flag = False
    for x in range(W):
        height = graph[x]
        if height >= y:
            if flag:
                cnt += temp
                temp = 0
            else:
                flag = True
        else:
            if flag:
                temp += 1
    answer += cnt
print(answer)