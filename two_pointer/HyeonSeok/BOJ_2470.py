import sys

N = int(sys.stdin.readline())
liqueur = list(map(int, sys.stdin.readline().split()))

# 정렬해서 양끝 조이기
liqueur.sort()
start, end = 0, N-1
min_value = sys.maxsize
min_idx = (0, 0)
while start != end:
    num = liqueur[start] + liqueur[end]
    if min_value > abs(num):
        min_value = abs(num)
        min_idx = (start, end)
    
    # 조이기 할 때 합이 더 작은쪽으로 조이기
    if abs(liqueur[start]+liqueur[end-1]) <= abs(liqueur[start+1]+liqueur[end]):
        end -= 1
    else:
        start += 1
print(liqueur[min_idx[0]], liqueur[min_idx[1]])