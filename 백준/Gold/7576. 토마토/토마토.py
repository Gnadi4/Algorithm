import sys
from collections import defaultdict, deque
input = sys.stdin.readline

m,n = map(int, input().rstrip().split())
box = [[0]*n for _ in range(m)]
dq = deque([])

for i in range(n):
    a = list(map(int, input().rstrip().split()))
    for j in range(m):
        box[j][i] = a[j]
        if a[j] == 1: dq.append((j,i))

ans = 0
while True:
    dq_tmp = deque([])
    while dq:
        j,i = dq.popleft()
        if j<m-1 and box[j+1][i]!=-1 and box[j+1][i]!=1:
            box[j+1][i]=1
            dq_tmp.append((j+1,i))
        if j>0 and box[j-1][i]!=-1 and box[j-1][i]!=1:
            box[j-1][i]=1
            dq_tmp.append((j-1,i))
        if i<n-1 and box[j][i+1]!=-1 and box[j][i+1]!=1:
            box[j][i+1]=1
            dq_tmp.append((j,i+1))
        if i>0 and box[j][i-1]!=-1 and box[j][i-1]!=1:
            box[j][i-1]=1
            dq_tmp.append((j,i-1))

    if not dq_tmp:
        break

    ans+=1
    dq = dq_tmp.copy()

chk = True
for i in range(n):
    for j in range(m):
        if box[j][i] == 0:
            chk = False
    if not chk: break

if chk: print(ans)
else: print(-1)