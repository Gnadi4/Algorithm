import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
if m!=0: list_m = list(map(int, input().rstrip().split()))

ans = float('inf')
if m == 10:
    ans = n-100
    if ans<0:
        ans*=-1
elif m == 0:
    ans = n-100
    if ans<0:
        ans*=-1
    ans = min(ans, len(str(n)))
else:
    ans = n-100
    if ans<0:
        ans*=-1
    val = 0
    while True:
        tmp = n-val
        if tmp>=0:
            for i in str(tmp):
                if int(i) in list_m:
                    tmp = -1
                    break
            if tmp != -1:
                ans = min(ans, len(str(tmp))+val)
                break
        tmp = n+val
        for i in str(tmp):
            if int(i) in list_m:
                tmp = -1
                break
        if tmp != -1:
            ans = min(ans, len(str(tmp))+val)
            break
        val+=1

print(ans)
