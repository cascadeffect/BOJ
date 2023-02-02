import sys

input = sys.stdin.readline

n = int(input())
score = list(map(int, input().split()))
m = max(score)
sum = 0

for i in range(len(score)):
  score[i] = (score[i] / m) * 100
  sum += score[i]

print(sum/len(score))