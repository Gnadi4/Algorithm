import sys
from collections import deque
import heapq

input = sys.stdin.readline

m,n,h = map(int, input().rstrip().split())

map_h = [[[0]*m for _ in range(n)] for _ in range(h)]

for i in range(h):
    for j in range(n):
        a = list(map(int, input().rstrip().split()))
        for k in range(m):
            map_h[i][j][k] = a[k]

q = deque([])
chk_h = [[[1]*m for _ in range(n)] for _ in range(h)]
res = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if chk_h[i][j][k] and map_h[i][j][k] == 1:
                # heapq.heappush(q,(0,i,j,k))
                q.append((0,i,j,k))
while q:
    num,a,b,c = q.popleft()
    res = max(res, num)
    if chk_h[a][b][c]:
        chk_h[a][b][c] = 0
        s_list = [(1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1)]
        for aa, bb, cc in s_list:
            if 0<=a+aa<h and 0<=b+bb<n and 0<=c+cc<m and chk_h[a+aa][b+bb][c+cc]:
                if map_h[a+aa][b+bb][c+cc] == 0:
                    map_h[a+aa][b+bb][c+cc] = 1
                    q.append((num+1, a+aa, b+bb, c+cc))

ans = 1
for i in range(h):
    for j in range(n):
        for k in range(m):
            if map_h[i][j][k] == 0:
                ans = 0

if ans:
    print(res)
else:
    print(-1)