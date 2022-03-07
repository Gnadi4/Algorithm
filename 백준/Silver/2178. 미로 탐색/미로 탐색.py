import sys
input = sys.stdin.readline

n,m = map(int,input().split())
list_m = [[0]*m for _ in range(n)]

for i in range(n):
    a = input()
    for j in range(m):
        if a[j] == "1":
            list_m[i][j] = 1

ans = 0
q = [[0,0,1]]
visited = []

while True:
    ind = q.pop(0)
    if ind[0]==n-1 and ind[1]==m-1:
        ans = ind[2]
        break
    if [ind[0], ind[1]] not in visited:
        visited.append([ind[0], ind[1]])
        if ind[0]>0 and list_m[ind[0]-1][ind[1]]==1:
            q.append([ind[0]-1, ind[1], ind[2]+1])
        if ind[1]>0 and list_m[ind[0]][ind[1]-1]==1:
            q.append([ind[0], ind[1]-1, ind[2]+1])
        if ind[0]<n-1 and list_m[ind[0]+1][ind[1]]==1:
            q.append([ind[0]+1, ind[1], ind[2]+1])
        if ind[1]<m-1 and list_m[ind[0]][ind[1]+1]==1:
            q.append([ind[0], ind[1]+1, ind[2]+1])

print(ans)