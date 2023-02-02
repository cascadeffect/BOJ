a, b = [int(i) for i in input().split(' ')] # 0 <= a <= 23 0, <= b <= 59
c = int(input()) # 0 <= c <= 1000

h = a
m = b + c

if m >= 60:
  h = h + int(m/60)
  if h >= 24:
    h = h - 24
  m = int(m%60)

print(h, m)