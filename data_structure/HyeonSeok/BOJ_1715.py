import heapq

N = int(input())
stacks = list()
for n in range(N):
    heapq.heappush(stacks, int(input()))
answer = 0
while len(stacks) > 1:
    a = heapq.heappop(stacks)
    b = heapq.heappop(stacks)
    add = a+b
    answer += add
    heapq.heappush(stacks, add)
print(answer)