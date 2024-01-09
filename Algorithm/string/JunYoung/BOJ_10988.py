# 팰린드롬인지 확인하기

import sys
word = sys.stdin.readline().strip()
N = len(word)

flag = True
#print(N//2)
for i in range(N//2):
    if word[i] != word[-(i+1)]:
        #print(word[i], word[-(i+1)])
        flag = False
        break

if flag:
    print(1)
else:
    print(0)

# -인덱스는 -1부터 시작