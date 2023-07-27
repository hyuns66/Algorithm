# 간판

import sys

N = int(sys.stdin.readline())
name = sys.stdin.readline().strip()

count = 0
for i in range(N):
    temp = sys.stdin.readline().strip()
    possible = set()
    for j in range(len(temp)):
        if temp[j] == name[0]:
            blank = 0
            flag = False
            while True:
                words = []
                for s in range(len(name)):
                    if j+s*(blank+1) < len(temp):
                        words.append(temp[j+s*(blank+1)])
                    else:
                        flag = True
                        break
                if flag:
                    break
                else:
                    str = ''.join(d for d in words)
                    possible.add(str)
                    blank += 1
    #print(possible)
    if name in possible:
        count += 1

print(count)
