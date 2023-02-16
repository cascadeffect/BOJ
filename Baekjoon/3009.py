import sys

x_set = set()
y_set = set()

for _ in range(3):
  x, y = (map(int, sys.stdin.readline().split()))
  if x not in x_set:
    x_set.add(x)
  else:
    x_set.remove(x)
  if y not in y_set:
    y_set.add(y)
  else:
    y_set.remove(y)

print(list(x_set)[0], list(y_set)[0])
  
