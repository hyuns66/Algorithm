import sys

N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
odds = list()
evens = list()
min_odd = 2*(10**9) + 1
min_even = 2*(10**9) + 1
for number in numbers:
    if number & 1:
        odds.append(number)
    else:
        evens.append(number)
# 홀홀끼리, 짝짝끼리 빼면 짝
for i in range(len(odds)-1):
    dif = abs(odds[i+1] - odds[i])
    min_even = min(min_even, dif)
for i in range(len(evens)-1):
    dif = abs(evens[i+1] - evens[i])
    min_even = min(min_even, dif)

if min_even == 2*(10**9) + 1:
    min_even = -1

if len(odds) == 0 or len(evens) == 0:
    min_odd = -1
else:
# 홀 짝 끼리 빼면 홀
    for i in range(N-1):
        if (numbers[i+1] & 1) ^ (numbers[i] & 1):
            dif = numbers[i+1] - numbers[i]
            min_odd = min(dif, min_odd)
            
print(min_even, min_odd)
