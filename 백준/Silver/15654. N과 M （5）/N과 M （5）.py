n,m = map(int, input().split())
list_n = list(map(int, input().split()))
list_n.sort()

def func(q, ind, cnt):
    if cnt == m:
        for i in q:
            print(i, end=' ')
        print()
        return
    for i in range(n):
        if list_n[i] not in q:
            func(q+[list_n[i]], i, cnt+1)
    return

func([],0,0)
