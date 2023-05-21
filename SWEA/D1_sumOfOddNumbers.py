T = int(input())
for case in range(1, T + 1):
  nums = list(map(int, input().split()))
  odds = []
  for num in nums:
    if num % 2 != 0:
      odds.append(num)
  print(f'#{case} {sum(odds)}')