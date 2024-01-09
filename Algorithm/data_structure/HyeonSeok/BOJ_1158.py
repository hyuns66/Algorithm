N, K = input().split()
N = int(N)
K = int(K)
people = [i for i in range(1, N+1)]
josephus = list()
target = 0

while len(people) != 0:
    target += K-1
    if target >= len(people):
        target = target%len(people)
    josephus.append(people.pop(target))

print("<", end='')
for i in range(0, N):
    if i == N-1:
        print(josephus[i], end = '>')
    else:
        print(str(josephus[i]), end=', ')
