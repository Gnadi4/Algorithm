import sys

input = sys.stdin.readline

x, y = map(int, input().rstrip().split())

mat = [[0]*y for _ in range(x)]
for i in range(x*2):
    tmp = list(map(int, input().rstrip().split()))
    for j in range(y):
        mat[i%x][j] += tmp[j]

for i in range(x):
    for j in range(y):
        print(mat[i][j],end=' ')
    print()