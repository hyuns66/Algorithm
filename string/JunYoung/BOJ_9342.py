# 염색체

import sys
T = int(sys.stdin.readline())
result = []
for i in range(T):
    dna = sys.stdin.readline().strip()
    letter = ['A', 'F', 'C']
    flag = True
    j=0
    for i in range(len(dna)):
        if (i!=0) and (i!=len(dna)):
            if dna[i] == letter[j]:
                continue
            elif (j+1 < len(letter)) and (dna[i] == letter[j+1]):
                j+=1
                continue
            else:
                flag = False
                break
    if flag:
        result.append("Infected!")
    else:
        result.append("Good")


for i in result:
    print(i)

"""
문자열은 {A, B, C, D, E, F} 중 0개 또는 1개로 시작해야 한다.
그 다음에는 A가 하나 또는 그 이상 있어야 한다.
그 다음에는 F가 하나 또는 그 이상 있어야 한다.
그 다음에는 C가 하나 또는 그 이상 있어야 한다.
그 다음에는 {A, B, C, D, E, F} 중 0개 또는 1개가 있으며, 더 이상의 문자는 없어야 한다.
문자열이 주어졌을 때, 위의 규칙을 만족하는지 구하는 프로그램을 작성하시오.
"""