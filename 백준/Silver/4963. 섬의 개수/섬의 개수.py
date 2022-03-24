import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

while True:
    w,h = map(int, input().rstrip().split())
    if w==0 and h==0: break
    list_m = [[0]*h for _ in range(w)]

    for i in range(h):
        a = list(map(int, input().rstrip().split()))
        for j in range(w):
            list_m[j][i] = a[j]
    
    def func(j,i):
        list_m[j][i]=0
        if j+1 < w and list_m[j+1][i]==1:
            func(j+1,i)
        if j+1 < w and i+1 < h and list_m[j+1][i+1]==1:
            func(j+1,i+1)
        if j+1 < w and i > 0 and list_m[j+1][i-1]==1:
            func(j+1,i-1)
        if i+1 < h and list_m[j][i+1]==1:
            func(j,i+1)
        if i+1 < h and j > 0 and list_m[j-1][i+1]==1:
            func(j-1,i+1)
        if j > 0 and i > 0 and list_m[j-1][i-1]==1:
            func(j-1,i-1)
        if j > 0 and list_m[j-1][i]==1:
            func(j-1,i)
        if i > 0 and list_m[j][i-1]==1:
            func(j,i-1)

        return
    ans = 0
    for i in range(h):
        for j in range(w):
            if list_m[j][i] == 1:
                func(j,i)
                ans += 1

    print(ans)