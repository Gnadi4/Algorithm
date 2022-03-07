import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

test = int(input().rstrip())
ans = []
for _ in range(test):
    n, m, t = map(int, input().rstrip().split())
    map_val = [[0]*m for _ in range(n)]
    for _ in range(t):
        x,y = map(int, input().rstrip().split())
        map_val[x][y] = 1

    def func(sx, sy):
        map_val[sx][sy] = 0
        if sx>0 and map_val[sx-1][sy]==1:
            func(sx-1, sy)
        if sy>0 and map_val[sx][sy-1]==1:
            func(sx, sy-1)
        if sx<n-1 and map_val[sx+1][sy]==1:
            func(sx+1, sy)
        if sy<m-1 and map_val[sx][sy+1]==1:
            func(sx, sy+1)
        return
    cnt=0
    for i in range(n):
        for j in range(m):
            if map_val[i][j]==1:
                func(i, j)
                cnt+=1
    ans.append(cnt)

for i in ans: print(i)

