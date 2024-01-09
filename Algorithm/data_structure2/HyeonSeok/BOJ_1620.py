import sys
from collections import deque

N, M = sys.stdin.readline().split()
N = int(N)
M = int(M)
pokemon = list()
answer = deque()

for i in range(N):
    # pokemon.append(sys.stdin.readline().strip())    # 개행문자까지 입력이 들어가기 때문에 strip()으로 제거
    pokemon.append(input())

for i in range(M):
    input = sys.stdin.readline().strip()
    if input.isdigit():     # readline()으로 들어오는 입력은 모두 문자열이므로 isdigit함수를 통해 숫자형인지 판별
        answer.append(pokemon[int(input)-1])
    else:
        answer.append(pokemon.index(input)+1)   # 포켓몬 인덱스는 1부터 시작하니까 +1

while answer:
    print(answer.popleft())