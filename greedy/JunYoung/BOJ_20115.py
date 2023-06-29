# 에너지 드링크  

import sys

N = int(sys.stdin.readline())
energyDrink = list(map(int, sys.stdin.readline().split()))

energyDrink.sort(reverse=True)
maxEnergy = energyDrink[0]
for i in range(1, N):
    maxEnergy += energyDrink[i] / 2

print(maxEnergy)

