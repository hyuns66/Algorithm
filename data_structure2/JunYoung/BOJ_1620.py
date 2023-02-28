# 나는야 포켓몬 마스터 이다솜

import sys

# 포켓몬의 개수 N, 내가 맞춰야하는 문제의 수 M
N, M = map(int, sys.stdin.readline().split())

dogam = []
answer = []
for i in range(N):
    pokemon = sys.stdin.readline().strip()
    dogam.append(pokemon)

for j in range(M):
    quiz = sys.stdin.readline().strip()
    if quiz.isdigit():
        answer.append(dogam[int(quiz)-1])
    else:
        answer.append(dogam.index(quiz)+1)

for i in answer:
    print(i)
