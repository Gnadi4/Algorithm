import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

from collections import deque

n,m = map(int, input().rstrip().split())
lab = [[0]*n for _ in range(m)]
q = deque([])
for i in range(n):
    a = list(map(int, input().rstrip().split()))
    for j in range(m):
        lab[j][i] = a[j]
        if a[j]==2: q.append((j,i))
res = []
def func(l, cnt, sx, sy):
    if cnt == 3:
        l_tmp = []
        q_tmp = q.copy()
        while q_tmp:
            j,i = q_tmp.popleft()
            if j+1 < m and l[j+1][i]==0:
                q_tmp.append((j+1,i))
                l[j+1][i]=2
                l_tmp.append((j+1,i))
            if j > 0 and l[j-1][i]==0:
                q_tmp.append((j-1,i))
                l[j-1][i]=2
                l_tmp.append((j-1,i))
            if i+1 < n and l[j][i+1]==0:
                q_tmp.append((j,i+1))
                l[j][i+1]=2
                l_tmp.append((j,i+1))
            if i > 0 and l[j][i-1]==0:
                q_tmp.append((j,i-1))
                l[j][i-1]=2
                l_tmp.append((j,i-1))

        ans = 0
        for i in range(n):
            for j in range(m):
                if l[j][i]==0:
                    ans += 1
        res.append(ans)
        while l_tmp:
            j,i = l_tmp.pop()
            l[j][i] = 0
        return
    else:
        while True:
            if sx==m: 
                if sy==n-1: break
                sx = 0
                sy += 1
            if l[sx][sy]==0:
                l[sx][sy]=1
                func(l, cnt+1, sx+1, sy)
                l[sx][sy]=0
            sx += 1
    return

func(lab, 0, 0, 0)
print(max(res))