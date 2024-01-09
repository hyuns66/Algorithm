# 파일 정리
# 딕셔너리 이용

import sys

N = int(sys.stdin.readline())

extensionDict = {}
for i in range(0, N):
    extension = list(sys.stdin.readline().split("."))[1]
    if extension in extensionDict:
        value = extensionDict.get(extension)
        extensionDict[extension] = value+1
    else:
        extensionDict[extension] = 1

extensionDict = dict(sorted(extensionDict.items()))
#key 기준으로 정렬가능 but,
#'key/n' 'value' 이렇게 저장되는 듯?
#=> 그래서 밑에 i.strip() 써줬다.

"""
딕셔너리 정렬방법
https://blockdmask.tistory.com/566
"""

for i in extensionDict:
    print(f"{i.strip()} {extensionDict[i]}")
