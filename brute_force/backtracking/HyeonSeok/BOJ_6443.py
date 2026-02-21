import sys
from collections import OrderedDict

def backTracking(depth, max_depth, word):
    global word_dict
    if depth == max_depth:
        print(word)
        return
    for key, value in word_dict.items():
        if value == 0:
            continue
        word += key
        word_dict[key] -= 1
        backTracking(depth+1, max_depth, word)
        word = word[:-1]
        word_dict[key] += 1

N = int(sys.stdin.readline())
words = []
for _ in range(N):
    temp = list(sys.stdin.readline().rstrip())
    words.append(temp)
    
for word in words:
    w_list = sorted(list(word)) # 철자 순으로 정렬해서 Dictionary에 각 철자 갯수 기록
    word_dict = OrderedDict()   # 철자 순서대로 출력해야 하므로 OrderedDict 사용
    for w in w_list:
        if w not in word_dict.keys():
            word_dict[w] = 1
        else:
            word_dict[w] += 1
    backTracking(0, len(w_list), "")