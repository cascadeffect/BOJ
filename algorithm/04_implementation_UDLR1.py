import sys

input = sys.stdin.readline

n = int(input())
x, y = 1, 1
plans = input().split()

move_types = ['L', 'R', 'U', 'D']
# 각각 plan이 L, R, U, D일 때 X, Y 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 이동 계획을 하나씩 확인
for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i]:
      # 이동할 좌표 = 현재 좌표 + 이동 방향
      nx = x + dx[i]
      ny = y + dy[i]
  # 공간을 벗어난 경우 무시
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  # 이동
  x, y = nx, ny

print(x, y)