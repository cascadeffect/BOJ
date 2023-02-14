import sys

input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))

sum = 0

for i in range(0, n):
  for j in range(i+1, n):
    for k in range(j+1, n):
      tmp = cards[i] + cards[j] + cards[k]
      if sum < tmp <= m:
        sum = tmp

print(sum)