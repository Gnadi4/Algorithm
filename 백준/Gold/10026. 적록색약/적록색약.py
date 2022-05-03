import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
map_n = []
for _ in range(n):
    map_n.append(input().rstrip())

chk_n = [[1]*n for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(n):
        if chk_n[i][j]:
            ans += 1
            q = deque([(i,j)])
            while q:
                p,z = q.popleft()
                d = [(1,0), (0,1), (-1,0), (0,-1)]
                if chk_n[p][z]:
                    chk_n[p][z] = 0
                    for l,m in d:
                        if 0 <= p+l < n and 0 <= z+m < n and chk_n[p+l][z+m]:
                            if map_n[p][z] == map_n[p+l][z+m]: 
                                q.append((p+l, z+m))

map_n_tmp = []
for i in map_n:
    map_n_tmp.append(i.replace('R','G'))

chk_n = [[1]*n for _ in range(n)]

res = 0
for i in range(n):
    for j in range(n):
        if chk_n[i][j]:
            res += 1
            q = deque([(i,j)])
            while q:
                p,z = q.popleft()
                d = [(1,0), (0,1), (-1,0), (0,-1)]
                if chk_n[p][z]:
                    chk_n[p][z] = 0
                    for l,m in d:
                        if 0 <= p+l < n and 0 <= z+m < n and chk_n[p+l][z+m]:
                            if map_n_tmp[p][z] == map_n_tmp[p+l][z+m]: 
                                q.append((p+l, z+m))


print(ans, res)
