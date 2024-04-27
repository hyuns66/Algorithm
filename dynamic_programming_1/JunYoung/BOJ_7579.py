# 앱
# 비활성화 했을 경우의 비용 ci의 합을 최소화하여 필요한 메모리 M 바이트를 확보하는 방법
import sys

n, m = map(int, sys.stdin.readline().split())
memory = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))

# 필요한 메모리 m 바이트를 확보하기 위한 최소비용을 계산

#============
#냅색 문제랑 비슷한 것 같으면서... 모르겠군.