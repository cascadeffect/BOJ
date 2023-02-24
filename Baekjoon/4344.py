import sys

input = sys.stdin.readline

C = int(input())

for i in range(C):
  scores = list(map(int, input().split()))
  N = scores.pop(0)
  avg = sum(scores) / N
  cnt = 0
  for score in scores:
    if score > avg:
      cnt += 1
  print(f"{'{:.3f}%'.format(cnt / N * 100)}")