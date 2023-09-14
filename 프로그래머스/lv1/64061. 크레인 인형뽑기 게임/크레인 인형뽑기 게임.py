import numpy as np

def solution(board, moves):
    answer = 0
    stack = []
    board = list(map(list, zip(*board)))
    for move in moves:
        idx = np.nonzero(board[move-1])[0]
        if len(idx):
            idx = idx[0]
        else:
            continue
        elm = board[move-1][idx]
        if len(stack) and elm == stack[-1]:
            stack.pop()
            answer += 2
        else:
            stack.append(elm)
        board[move-1][idx] = 0
    return answer