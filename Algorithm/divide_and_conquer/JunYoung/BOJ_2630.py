# 색종이 만들기

import sys

N = int(sys.stdin.readline())
arr = [[0 for j in range(N)] for i in range(N)]
white = 0
blue = 0


def cutPaper(paper_array):
    #print(paper_array)
    #print("----------------")
    N_array = len(paper_array)
    refPoint = paper_array[0][0]
    flag = 0
    global blue
    global white

    for i in range(N_array):
        for j in range(N_array):
            if paper_array[i][j] != refPoint:
                flag = 1  # 다른게 섞여있으므로, 더 잘라야함
                break

    if flag:
        if N_array == 1:
            if refPoint == '1':
                blue += 1
            else:
                white += 1
        else:
            cutPaper([row[:N_array // 2] for row in paper_array[:N_array // 2]])  # 왼쪽 위
            cutPaper([row[N_array // 2:] for row in paper_array[:N_array // 2]])  # 오른쪽 위
            cutPaper([row[:N_array // 2] for row in paper_array[N_array // 2:]])  # 왼쪽 아래
            cutPaper([row[N_array // 2:] for row in paper_array[N_array // 2:]])  # 오른쪽 아래
            #cutPaper(paper_array[0:int(N_array / 2)][0:int(N_array / 2)])  # 왼쪽 위
            #cutPaper(paper_array[0:int(N_array / 2)][int(N_array / 2):])  # 오른쪽 위
            #cutPaper(paper_array[int(N_array / 2):][0:int(N_array / 2)])  # 왼쪽 아래
            #cutPaper(paper_array[int(N_array / 2):][int(N_array / 2):])  # 오른쪽 아래
    else:
        if refPoint == '1':
            blue += 1
        else:
            white += 1


for i in range(N):
    temp = list(sys.stdin.readline().strip().split())
    for j in range(N):
        arr[i][j] = temp[j]

cutPaper(arr)

print(white)
print(blue)
