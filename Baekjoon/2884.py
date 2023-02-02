h, m = [int(i) for i in input().split(' ')]
if 45 <= m <= 59:
  m = m - 45
else:
  if h == 0 :
    h = 23
  else:
    h = h - 1
  m = 60 - (45 - m)
print(h, m)