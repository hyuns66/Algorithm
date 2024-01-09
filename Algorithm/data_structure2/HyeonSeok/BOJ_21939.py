import sys
import heapq

N = int(sys.stdin.readline())
boj = dict()
easy = list()
hard = list()
dif_set_max = dict()
dif_set_min = dict()

for i in range(N):
    b = list(map(int, sys.stdin.readline().split()))
    boj[b[0]] = [True, b[1]]
    heapq.heappush(easy, (b[1], b[0]))  # 난이도 , 인덱스
    heapq.heappush(hard, (-b[1], -b[0]))
    if b[1] in dif_set_max:                 # 딕셔너리에 난이도 인덱스로 접근해서 문제번호 쭉 가져올 수 있게 저장
        heapq.heappush(dif_set_max[b[1]], -b[0])
        heapq.heappush(dif_set_min[b[1]], b[0])
    else:
        dif_set_max[b[1]] = [-b[0]]
        dif_set_min[b[1]] = [b[0]]

# 명령어 저장
op = list()
M = int(sys.stdin.readline())
for j in range(M):
    op.append(list(sys.stdin.readline().split()))


for j in range(M):
    if op[j][0] == "recommend":
        par = int(op[j][1])
        if par == 1:
            while not boj[-hard[0][1]][0]:
                heapq.heappop(hard)
            temp = hard[0]
            while not boj[-dif_set_max[-temp[0]][0]][0]:
                heapq.heappop(dif_set_max[-temp[0]])
            print(-dif_set_max[-temp[0]][0])
        elif par == -1:
            while not boj[easy[0][1]][0]:
                heapq.heappop(easy)
            temp = easy[0]
            while not boj[dif_set_min[temp[0]][0]][0]:
                heapq.heappop(dif_set_min[temp[0]])
            print(dif_set_min[temp[0]][0])
    elif op[j][0] == "add":
        num, dif = int(op[j][1]), int(op[j][2])
        heapq.heappush(easy, (dif, num))
        heapq.heappush(hard, (-dif, -num))
        if dif in dif_set_max:
            heapq.heappush(dif_set_max[dif], -num)
            heapq.heappush(dif_set_min[dif], num)
        else:
            dif_set_max[dif] = [-num]
            dif_set_min[dif] = [num]
        boj[num] = [True, dif]
    elif op[j][0] == "solved":
        par = int(op[j][1])
        boj[par][0] = False
        dif = boj[par][1]
        temp = list()
        while -dif_set_max[dif][0] != par:
            temp.append(heapq.heappop(dif_set_max[dif]))
        heapq.heappop(dif_set_max[dif])
        while temp:
            heapq.heappush(dif_set_max[dif], temp.pop())
        while dif_set_min[dif][0] != par:
            temp.append(heapq.heappop(dif_set_min[dif]))
        heapq.heappop(dif_set_min[dif])
        while temp:
            heapq.heappush(dif_set_min[dif], temp.pop())
