T = int(input())

# direction이 0(우), 1(하), 2(좌), 3(상) 일 때 이동 속도
dx = [0, 1, 0, -1] # 가로
dy = [1, 0, -1, 0] # 세로

for case in range(1, T + 1):
  n = int(input())
  snail = [[0] * n for _ in range(n)]

  x, y = 0, -1 # 현재 위치
  direction = 0 # 이동 방향: 0(우), 1(하), 2(좌), 3(상)
  num = 1 # 저장할 숫자
  
  while n > 0:
    for _ in range(n):
      # 이동 방향으로 이동 거리만큼 이동
      x += dx[direction]
      y += dy[direction]
      # 숫자 저장 후 1씩 증가
      snail[x][y] = str(num)
      num += 1
    direction = (direction + 1) % 4
    # 이동 방향이 홀수(상하)가 될 때마다 n을 1씩 감소 (달팽이 모양이 안쪽으로 갈수록 줄어드는 특성 때문)
    if direction % 2 != 0:
      n -= 1

  print(f'#{case}')
  for row in snail:
    print(" ".join(row))

# 3
# 1 2 3
# 8 9 4
# 7 6 5

# 4
# 1   2   3   4
# 12  13  14  5
# 11  16  15  6
# 10  9   8   7

# 5
# 1   2   3   4   5
# 16  17  18  19  6
# 15  24  25  20  7
# 14  23  22  21  8
# 13  12  11  10  9

# 6
# 1   2   3   4   5   6
# 20  21  22  23  24  7
# 19  32  33  34  25  8
# 18  31  36  35  26  9
# 17  30  29  28  27  10
# 16  15  14  13  12  11