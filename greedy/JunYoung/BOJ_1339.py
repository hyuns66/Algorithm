# 단어 수학
# 그리디의 대상이 무엇인지 고민해보고 푸는 것이 중요!

import sys

N = int(sys.stdin.readline())

dict = {}
for i in range(N):
    str = sys.stdin.readline().strip()
    for s in range(1, len(str)+1):
        word = str[-s]
        if word in dict:
            dict[word] += 10 ** (s-1)
        else:
            dict[word] = 10 ** (s-1)

sorted_list = sorted(dict.items(), key=lambda x:-x[1])
#print(sorted_list)

val = 9
answer = 0
for i in sorted_list:
    answer += i[1] * val
    val -= 1

print(answer)