# 멀티버스 1
import sys

M, N = map(int, sys.stdin.readline().split())

planet = []
for i in range(M):
    input = list(sys.stdin.readline().split())
    temp = []
    for j in range(1, N+1):
        temp.append([j,input[j-1]])
    temp.sort(key = lambda x:x[-1])

    temp2 = []
    for i in range(len(temp)):
        temp2.append(temp[i][0])
    planet.append(temp2)

#print(planet)

count = 0
for i in range(M-1):
    for j in range(i+1, M):
        if planet[i] == planet[j]:
            count += 1
print(count)
