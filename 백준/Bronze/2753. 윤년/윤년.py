import sys

input = sys.stdin.readline

inp = int(input().rstrip())

print(1 if ((inp % 4 == 0 and inp % 100 != 0) or (inp % 400 == 0)) else 0)