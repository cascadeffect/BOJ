for case in range(1, 11):
  N = int(input())
  buildings = list(map(int, input().split()))
  count = 0
  for i in range(2, len(buildings)-2):
    first = [buildings[i] - buildings[i-1], buildings[i] - buildings[i+1]]
    if first[0] > 0 and first[1] > 0:
      second = [buildings[i] - buildings[i-2], buildings[i] - buildings[i+2]]
      if second[0] > 0 and second[1] > 0:
        count += min(min(first[0], second[0]), min(first[1], second[1]))
  print(f'#{case} {count}')