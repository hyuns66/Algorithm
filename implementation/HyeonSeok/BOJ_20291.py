import sys

N = int(sys.stdin.readline())
files = dict()
for _ in range(N):
    file = list(sys.stdin.readline().rstrip().split('.'))
    if file[1] in files:
        files[file[1]] += 1
    else:
        files[file[1]] = 1

files_idx = sorted(files)
for f in files_idx:
    print(f, files[f])

