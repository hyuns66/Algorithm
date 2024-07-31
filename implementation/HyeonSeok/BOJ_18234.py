N, T = map(int, input().split())
carrots = list()
for _ in range(N):
    w, p = map(int, input().split())
    carrots.append([p, w+p*(T-1)])
carrots.sort()
answer = carrots.pop()[1]
day = 1
while carrots:
    p, w = carrots.pop()
    answer += w-p*day
    day += 1
print(answer)
