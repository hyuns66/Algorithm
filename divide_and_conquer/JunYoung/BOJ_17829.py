# 222-풀링

import sys

N = int(sys.stdin.readline())
arr = [[0 for j in range(N)] for i in range(N)]


def pooling222(array):
    M = int(len(array) / 2)
    arr = [[0 for j in range(M)] for i in range(M)]


    for i in range(M):
        for j in range(M):
            orderList = []
            for m in range(2):
                for n in range(2):
                    orderList.append(array[2 * i + m][2 * j + n])
            orderList.sort()
            #print(orderList)
            #print("-----------")
            arr[i][j] = orderList[2]  # index2는 3번째로 큰 수

    #print(arr)

    if M == 1:
        print(arr[0][0])
        #return arr[0][0]
    else:
        pooling222(arr)


for i in range(N):
    temp = list(sys.stdin.readline().strip().split())
    for j in range(N):
        arr[i][j] = int(temp[j])

pooling222(arr)

# 숫자비교 str형으로 비교하면 안되나..?
