def solution(board):
    string = "".join(board)
    
    ocnt = string.count("O")
    xcnt = string.count("X")
    
    # O가 X보다 2개 이상 많거나 X가 O보다 1개 이상 많음
    if ocnt-xcnt >= 2 or xcnt-ocnt >= 1:
        return 0
    
    def isWin(row, col, ox):
        if row.count(ox) == 3 or col.count(ox) == 3:
            return True
    
    diagonal = [(string[0], string[4], string[8]), (string[2], string[4], string[6])]
    
    # O가 대각선으로 이겼는데 X를 더 그림
    if isWin(diagonal[0], diagonal[1], "O") and xcnt >= ocnt:
        return 0
    # X가 대각선으로 이겼는데 O를 더 그림
    if isWin(diagonal[0], diagonal[1], "X") and xcnt < ocnt:
        return 0
    
    rotation = list(zip(*board))
    
    for i in range(3):
        # O가 가로 또는 세로로 이겼는데 X를 더 그림
        if isWin(board[i], rotation[i], "O") and xcnt >= ocnt:
            return 0
        # X가 가로 또는 세로로 이겼는데 X를 더 그림
        if isWin(board[i], rotation[i], "X") and xcnt < ocnt:
            return 0
    
    return 1