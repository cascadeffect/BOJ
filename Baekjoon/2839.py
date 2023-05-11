import sys

N = int(sys.stdin.readline())

q, r = divmod(N, 5)

if r:
  print(q)
else:
  bag = q
  q, r = divmod(r, 3)
  if r:
    print(bag + q)
  else:
    print(-1)