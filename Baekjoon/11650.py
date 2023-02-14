import sys

input = sys.stdin.readline

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

sorted_xy = sorted(xy, key = lambda elem : (elem[0], elem[1]))

for x, y in sorted_xy:
  print(x, y)