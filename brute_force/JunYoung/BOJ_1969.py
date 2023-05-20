# DNA

import sys
N, M = map(int, sys.stdin.readline().split())

dnaMoum = {}

for i in range(0, M):
    dnaMoum[i] = []  # 각 키에 빈 리스트 할당

for i in range(N):
    dna = sys.stdin.readline().strip()
    for j in range(M):
        dnaMoum[j].append(dna[j])

answer = []
hd = 0

for i in range(M):
    maxDict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    colList = dnaMoum[i]
    #print(colList)
    for j in colList:
        maxDict[j] += 1
    max_key = max(maxDict, key=maxDict.get)
    answer.append(max_key)
    values_list = list(maxDict.values())
    values_list.sort(reverse=True)
    for i in range(1, len(values_list)):
        hd += values_list[i]

for i in answer:
    print(i, end='')
print()
print(hd)

# dictionary를 많이 까먹은것 같다.. -05/20