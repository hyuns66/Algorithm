import heapq

N = int(input())
A = sorted(list(map(int, input().split())))
B = list(map(int, input().split()))
h = list()
for idx, num in enumerate(B):
    heapq.heappush(h,(-num, idx))
answer = 0
idx = 0
while h:
    num, _ = heapq.heappop(h)
    answer -= num*A[idx]
    idx += 1
print(answer)