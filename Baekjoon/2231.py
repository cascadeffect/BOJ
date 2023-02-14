import sys

n = int(sys.stdin.readline())

subtotal = 0

for i in range(n):
  subtotal += i
  tmp = i
  for j in range(len(str(i))):
    subtotal += tmp % 10
    tmp = tmp // 10
  if subtotal == n:
    print(i)
    break
  else:
    subtotal = 0

if subtotal == 0:
  print(0)