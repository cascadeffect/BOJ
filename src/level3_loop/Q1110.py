n = int(input())
tmp = n
count = 0
new = 0

while True:
  buf = tmp//10 + tmp%10
  new = (tmp%10)*10 + buf%10
  tmp = new
  count += 1;
  if new == n:
    break

print(count)