import sys

x, y, w, h = map(int, sys.stdin.readline().split())

print(min([x, y, abs(x-w), abs(y-h)]))