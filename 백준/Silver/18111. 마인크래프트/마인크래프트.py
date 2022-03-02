import sys
input = sys.stdin.readline
n,m,b = map(int,input().split())

mine = []
ma = 0
ans = [float("inf"),0]

for i in range(n):
    mine.append(list(map(int,input().split())))
    ma = max(ma, max(mine[-1]))

for i in range(n):
    for j in range(m):
        mine[i][j] = ma - mine[i][j]

for k in range(ma+1):
    tmp = 0
    blo = 0
    b_tmp = 0
    for i in range(n):
        for j in range(m):
            if mine[i][j]>0:
                tmp+=mine[i][j]
                blo+=mine[i][j]
                mine[i][j] -= 1
            else:
                tmp+=-2*mine[i][j]
                mine[i][j] -= 1
                b_tmp += 1
    if ans[0] > tmp and blo <= b:
        ans[0] = tmp
        ans[1] = ma-k
    elif ans[0] == tmp and blo <= b:
        break
    elif ans[0] < tmp:
        break

    b += b_tmp
print(ans[0],ans[1])