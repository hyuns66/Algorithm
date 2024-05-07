# 중앙값 구하기
import sys, heapq

T = int(sys.stdin.readline())

answers = []
for _ in range(T):
    #print("========테스트 시작============")

    M = int(sys.stdin.readline())
    array = []
    while len(array) < M:
        array += list(map(int, sys.stdin.readline().split()))

    answer = [array[0]]
    max_h = [-array[0]]
    min_h = []
    for i in range(1,len(array)):
        #print(f"{(i+1)}번째 수 ")
        if array[i] <= -max_h[0]:
            heapq.heappush(max_h, -array[i])
        else:
            heapq.heappush(min_h, array[i])

        if len(min_h) > len(max_h): # max_h이 min_h보다 크게 유지
            min_val = heapq.heappop(min_h)
            heapq.heappush(max_h, -min_val)
        elif len(max_h) > len(min_h) + 1:
            min_val = heapq.heappop(max_h)
            heapq.heappush(min_h, -min_val)

        if (i + 1) % 2 != 0:  # 홀수면
            answer.append(-max_h[0])  # 중앙값 추가
            #print(f"max_heap = {max_h}")
            #print(f"min_heap = {min_h}")

    answers.append(answer)

for a in answers:
    print(len(a))
    for i in range(len(a)):
        if i!=0 and i % 10 == 0:
            print()
        print(a[i], end=" ")
    print()