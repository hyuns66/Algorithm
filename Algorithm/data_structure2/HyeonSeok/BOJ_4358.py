import sys
import heapq

total = 0
trees = []
tree_cnt = 1
tree_dict = dict()

while True:
    input = sys.stdin.readline().strip()    # 계속해서 입력받음
    if not input:
        break
    else:
        total += 1
        heapq.heappush(trees, input)    # 총 나무 수 카운트하면서 정렬하기 위해 최소힙 사용

while trees:
    tree = heapq.heappop(trees)     # 최소힙에서 pop 하면 사전순으로 나무 튀어나옴 A~Z
    if tree in tree_dict:
        tree_dict[tree] += 1        # 똑같은나무 나오면 개수만 증가
    else:
        tree_dict[tree] = 1         # 새로운 나무 나오면 딕셔너리에 추가

keyList = list(tree_dict.keys())
keyList.sort()              # 딕셔너리의 나무 key값들을 리스트로 만들어서 정렬
for key in keyList:         # 정렬된 key값들 가져와서 평균 구하고 출력
    print("%s %.4f" % (key, tree_dict[key] / total * 100))