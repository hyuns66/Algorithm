def make_subsets(S, idx, subsets, temp):
    for i in range(idx, len(S)):
        temp.append(S[i])
        subsets.append(temp[:])
        make_subsets(S, i+1, subsets, temp[:])
        temp.pop()
        
def everage(s):
    sum = 0
    for num in s:
        sum += num
    return sum / len(s)

T = int(input())
    
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    S = list(map(int, input().split()))
    subsets = list()
    make_subsets(S, 0, subsets, list())
    sum = 0
    for s in subsets:
        sum += everage(s)
    print(f"#{test_case}", "{:.16f}".format(sum / len(subsets)).rstrip('0').rstrip('.'))
    # ///////////////////////////////////////////////////////////////////////////////////
