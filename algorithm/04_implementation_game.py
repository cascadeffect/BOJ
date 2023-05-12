import sys

input = sys.stdin.readline
n, m = map(int, input().split())
x, y, direction = map(int, input().split()) # 현재 좌표와 바라보고 있는 방향
map_list = [list(map(int, input().split())) for _ in range(n)]

d = [[0] * m for _ in range(n)] # 방문한 위치를 저장하기 위한 맵
d[x][y] = 1 # 입력받은 현재 좌표 방문 처리

# 북, 동, 남, 서 방향에 따른 이동 방향
direction_type = [0, 1, 2, 3] # 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3

visit_cnt = 1 # 방문한 좌표 개수
turn_cnt = 0 # 한 좌표에서 회전한 횟수
while True:
  # 왼쪽으로 회전
  turn_left()
  # 이동할 좌표 = 현재 좌표 + 이동 방향
  nx = x + dx[direction]
  ny = y + dy[direction]
  # 회전 후 정면에 가보지 않은 칸이 있고 바다가 아닌 경우 이동 수행
  if d[nx][ny] == 0 and map_list[nx][ny] == 0:
    d[nx][ny] = 1
    x = nx
    y = ny
    visit_cnt += 1
    turn_cnt = 0
    continue
  # 회전 후 정면에 가보지 않은 칸이 없거나 바다인 경우
  else:
    turn_cnt += 1
    # 해당 좌표에서 네 방향 모두 갈 수 없는 경우
    if turn_cnt == 4:
      # 뒤로 이동했을 때의 좌표
      nx = x - dx[direction]
      ny = y - dy[direction]
      # 뒤가 육지인 경우 뒤로 이동 수행
      if map_list[nx][ny] == 0:
        x = nx
        y = ny
      # 뒤가 바다인 경우
      else:
        break
      turn_cnt = 0

print(visit_cnt)
