# 전공책

import sys
import itertools

T = sys.stdin.readline().strip()
N = int(sys.stdin.readline())
price = []
book = {}

for i in range(N):
    book[i] = []

for i in range(N):
    P, name = map(str, sys.stdin.readline().split())
    price.append(int(P))
    for j in name:
        book[i].append(j)

temp = []
flag = True
for i in range(len(T)):
    bookIdx = []
    #print(T[i])
    for j in range(len(book)):
        #print(j)
        #print(book[j])
        if T[i] in book[j]:
            bookIdx.append(j)  # 책 인덱스 추가
    if len(bookIdx) == 0:
        flag = False
        break
    temp.append(bookIdx)

#print(temp)

if flag == False:
    print(-1)
else:
    combinations = list(itertools.product(*temp))

    answer = []
    for i in combinations:
        tempBook = {}

        for a in range(N):
            tempBook[a] = []

        for a in range(N):
            b = book[a]
            for j in b:
                tempBook[a].append(j)

        flag2 = True
        #print(i)
        for j in range(len(i)): #가능한 경우 한 세트를 돌면서
            if T[j] in tempBook[i[j]]:
                tempBook[i[j]].remove(T[j])
            else:
                #print("없다")
                flag2 = False
                break

        if flag2: #가능한 조합이면,
            s = set(i)
            #print("가능한 조합")
            #print(s)
            p = 0
            for i in s:
                p += price[i]
            answer.append(p)

    # print(combinations)
    # print(answer)

    answer.sort()
    print(answer[0])

# AAA
# 3
# 10000 BCD
# 20000 AAC
# 50000 DDD