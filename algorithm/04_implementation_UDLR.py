import sys

input = sys.stdin.readline

n = int(input())
x, y = 1, 1
plans = input().split()

for plan in plans:
  if plan == 'U':
    if y == 1:
      continue
    y -= 1
  elif plan == 'D':
    if y == n:
      continue
    y += 1
  elif plan == 'L':
    if x == 1:
      continue
    x -= 1
  elif plan == 'R':
    if x == n:
      continue
    x += 1

print(y, x)