# 이진수 덧셈

import sys
T = int(sys.stdin.readline())
answers= []

for i in range(T):
    A, B = map(str, sys.stdin.readline().strip().split())
    maxNum = max(len(A), len(B))
    nA = ['0' for i in range(maxNum + 1)]
    for i in range(len(A)):
        nA[-(i+1)] = A[-(i+1)]
    nB = ['0' for i in range(maxNum+1)]
    for i in range(len(B)):
        nB[-(i+1)] = B[-(i+1)]
    answer = [0 for i in range(maxNum+1)]
    addition = 0

    for j in range(maxNum):
        #print("< j: " + str(j)+ ">")
        #print("addtion = " + str(addition) +"/ nA = "+ str(nA) + "/ nB = "+ str(nB) )
        if addition == 0:
            if nA[-(j + 1)] == '0' and nB[-(j + 1)] == '0':
                answer[-(j + 1)] = 0
            elif nA[-(j + 1)] == '0' and nB[-(j + 1)] == '1':
                answer[-(j + 1)] = 1
            elif nA[-(j + 1)] == '1' and nB[-(j + 1)] == '0':
                answer[-(j + 1)] = 1
            elif nA[-(j + 1)] == '1' and nB[-(j + 1)] == '1':
                answer[-(j + 1)] = 0
                addition = 1
        else:
            if nA[-(j + 1)] == '0' and nB[-(j + 1)] == '0':
                answer[-(j + 1)] = 1
                addition = 0
            elif nA[-(j + 1)] == '0' and nB[-(j + 1)] == '1':
                answer[-(j + 1)] = 0
                addition = 1
            elif nA[-(j + 1)] == '1' and nB[-(j + 1)] == '0':
                answer[-(j + 1)] = 0
                addition = 1
            elif nA[-(j + 1)] == '1' and nB[-(j + 1)] == '1':
                answer[-(j + 1)] = 1
                addition = 1
    if addition == 1:
        answer[0] = 1

    #print(answer)
    count = 0
    for i in answer:
        if i == 1:
            break
        else:
            count +=1
    if count == len(answer):
        answers.append('0')
    else:
        answers.append(''.join(map(str, answer[count:])))

for i in answers:
    print(i)

# 앞에 0 다 제거함

# 다른 반례
# 1
# 00000000000000000000000 000000000000000000000000000000000000000000000000000000000000
