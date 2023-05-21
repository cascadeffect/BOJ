T = int(input())
for case in range(1, T + 1):
  n = int(input())
  sale_price = list(map(int, input().split()))
  
  max_num = 0
  profit = 0
  
  for price in sale_price[::-1]:
    if price > max_num:
      max_num = price
    else:
      profit += max_num - price

  print(f'#{case} {profit}')