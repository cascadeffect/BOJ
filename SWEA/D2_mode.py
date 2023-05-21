T = int(input())
for case in range(1, T + 1):
  num = int(input())
  scores = sorted(list(map(int, input().split())))
  count = [0] * 101
  score_i = 0
  for count_i in range(102):
    while score_i < len(scores):
      if count_i == scores[score_i]:
        count[count_i] += 1
      else:
        break
      score_i += 1
  
  mode = 100 - count[::-1].index(max(count))
  print(f'#{case} {mode}')