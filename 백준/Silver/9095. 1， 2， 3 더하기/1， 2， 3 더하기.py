import sys
input = sys.stdin.readline

test = int(input().rstrip())
list_n = [1,2,3]

def func(n):
    ret = 0

    if n == 0: return 1
    elif n < 0: return 0

    for i in list_n:
        ret += func(n-i)
    
    return ret

for _ in range(test):
    n = int(input().rstrip())
    
    print(func(n))
