# 접미사 배열

import sys

S = sys.stdin.readline().strip()

suffix = []
for i in range(0, len(S)):
    suffix.append(S[i:].strip())

suffix.sort()

for i in suffix:
    print(i.strip())

# S를 입력받을 때, strip을 안해서, 답에 \n까지 포함이 되어서 출력형식이 잘못되었다는 문구가 뜬 것 같다.
