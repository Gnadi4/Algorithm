import sys

input = sys.stdin.readline

while(True):
    n, m = map(int, input().rstrip().split())
    if n == 0 and m == 0:
        break
    if n > m:
        print("Yes")
    else:
        print("No")