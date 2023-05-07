import sys

input = sys.stdin.readline

li = list(map(int, input().rstrip().split()))

to = 0
for i in li:
    to += i**2
print(to%10)