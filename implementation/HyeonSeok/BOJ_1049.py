import sys

N, M = map(int, input().split())
min_bundle = sys.maxsize
min_each = sys.maxsize
package_num = N // 6
each_num = N % 6
for _ in range(M):
    bundle, each = map(int, input().split())
    min_bundle = min(bundle, min_bundle)
    min_each = min(each, min_each)
if min_bundle < min_each*6: # 패키지가 싼 경우
    answer = min_bundle * package_num + min_each * each_num
    answer = min(answer, min_bundle*(package_num+1))
    print(answer)
else:
    print(min_each * N)