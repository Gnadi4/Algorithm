import sys

input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()

print('go' if len(a) >= len(b) else 'no')