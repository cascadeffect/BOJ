import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nxm_board = [input().rstrip() for _ in range(n)]

fin_count = []

for i in range(n-7):
  mid_count = []
  for j in range(m-7):
    chk_board = []
    # chk_board[0][0]을 B로 할 경우와 W로 할 경우를 다 생각해서 어떤 경우가 더 적은 색칠 횟수를 갖는지 판별해야 함
    b_count = 0 # 시작을 'B'라고 가정했을 때 색칠 횟수 (2n열이 'B', 2n-1열이 'W')
    w_count = 0 # 시작을 'W'라고 가정했을 때 색칠 횟수 (2n열이 'W', 2n-1열이 'B')
    for k in range(8):
      chk_board.append(nxm_board[i+k][j:j+8])
      for l in range(8):
        # chk_board[k][l]이 2n열일 경우
        if (k+l) % 2 == 0:
          # 2n열이 'B'일 경우
          if chk_board[k][l] == 'B':
            # 시작을 'W'라고 가정했을 때 색칠 횟수 +1
            w_count += 1
          # 2n열이 'W'일 경우
          else:
            # 시작을 'B'라고 가정했을 때 색칠 횟수 +1
            b_count += 1
        # chk_board[k][l]이 2n-1열일 경우
        else:
          # 2n-1열이 'B'일 경우
          if chk_board[k][l] == 'B':
            # 시작을 'B'라고 가정했을 때 색칠 횟수 +1
            b_count += 1
          # 2n-1열이 'W'일 경우
          else:
            # 시작을 'W'라고 가정했을 때 색칠 횟수 +1
            w_count += 1
    mid_count.append(b_count if b_count < w_count else w_count)
  fin_count.append(min(mid_count))

print(min(fin_count))