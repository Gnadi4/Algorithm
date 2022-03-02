import sys
input = sys.stdin.readline

k,n = map(int,input().split())
list_k = []
max_val = 0
cur_val = 1
ans = 0

for i in range(k):
    list_k.append(int(input()))
    max_val = max(max_val, list_k[-1])

while max_val - cur_val >= 0:
    mid_val = (max_val+cur_val)//2
    count_val = 0
    for i in list_k:
        count_val += i//mid_val
    
    if count_val >= n:
        ans = max(ans, mid_val)
        cur_val = mid_val+1
    else:
        max_val = mid_val-1

print(ans)