import sys
input = sys.stdin.readline

n = int(input())
map_val = []

for _ in range(n):
    map_val.append(list(map(int,list(input().rstrip()))))

ans=[]

def func(sx, sy):
    tmp_val = 0
    if map_val[sx][sy]==1:
        tmp_val = 1
        map_val[sx][sy]=0
    
    if sx>0 and map_val[sx-1][sy]==1:
        tmp_val+=func(sx-1, sy)
    if sy>0 and map_val[sx][sy-1]==1:
        tmp_val+=func(sx, sy-1)
    if sx<n-1 and map_val[sx+1][sy]==1:
        tmp_val+=func(sx+1, sy)
    if sy<n-1 and map_val[sx][sy+1]==1:
        tmp_val+=func(sx, sy+1)
    
    return tmp_val

for i in range(n):
    for j in range(n):
        co = 0
        if map_val[i][j]==1:
            co += func(i, j)
            ans.append(co)

print(len(ans))
ans.sort()
for i in ans: print(i)