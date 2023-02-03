import sys

board = [list(map(int, sys.stdin.readline().split())) for i in range(9)]

max = 0
col = 0
row = 0

for i in range(9):
    for j in range(9):
        if board[i][j] > max:
            max = board[i][j]
            col = j
            row = i

print(max)
print(row + 1, col + 1)