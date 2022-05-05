n,m = map(int, input().split())

def func(q, cnt):
    if cnt == m:
        for i in q:
            print(i, end=' ')
        print()
        return
    if q:
        for i in range(q[-1], n+1):
            func(q+[i], cnt+1)
    else:
        for i in range(1,n+1):
            func(q+[i], cnt+1)
    return

func([],0)
