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
# for i in range(N-1):
#     m = 0
#     for c in carrots:
#         c[0] -= c[1]
#         m = max(m, c[0])
#     carrots.sort()
#     answer += carrots.pop()[0]
# print(answer)