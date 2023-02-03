import sys

input = sys.stdin.readline

n = int(input().rstrip())
coordinates = [list(map(int, input().split())) for _ in range(n)]

# paper[0][0] == False => 원점으로부터 x축, y축 전부 0~1씩 덮여 있음
paper = [[0 for _ in range(100)] for _ in range(100)]

for i in range(n):
    left = coordinates[i][0]
    bottom = coordinates[i][1]
    for j in range(10):
      for k in range(10):
        paper[bottom + j][left + k] = 1

count = 0

for p in paper:
  count += p.count(1)

print(count)