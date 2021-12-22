def findType(board, p, q):
    val = board[p][q]
    if p+1 < len(board) and q+2 < len(board) and (board[p+1][q] == board[p+1][q+1] == board[p+1][q+2] == val):
        return 1
    if p-1 >= 0 and q+2 < len(board) and (board[p][q+1] == board[p][q+2] == board[p-1][q+2] == val):
        return 2
    if p+2 < len(board) and q+1 < len(board) and (board[p+1][q] == board[p+2][q] == board[p+2][q+1] == val):
        return 3
    if p-2 >= 0 and q+1 < len(board) and (board[p][q+1] == board[p-1][q+1] == board[p-2][q+1] == val):
        return 4
    if p-1 >= 0 and q+2 < len(board) and (board[p][q+1] == board[p-1][q+1] == board[p][q+2] == val):
        return 5
    return 0

def isTop(board, p, q):
    for i in range(0, p):
        if board[i][q] != 0:
            return False
    return True

def isRemovable(board, p, q, t):
    if t == 1:
        if isTop(board, p+1, q+1) and isTop(board, p+1, q+2):
            return True
    if t == 2:
        if isTop(board, p, q) and isTop(board, p, q+1):
            return True
    if t == 3:
        if isTop(board, p+2, q+1):
            return True
    if t == 4:
        if isTop(board, p, q):
            return True
    if t == 5:
        if isTop(board, p, q) and isTop(board, p, q+2):
            return True
    return False

def remove(board, p, q, t):
    board[p][q] = 0
    if t == 1:
        board[p+1][q] = board[p+1][q+1] = board[p+1][q+2] = 0
    if t == 2:
        board[p][q+1] = board[p][q+2] = board[p-1][q+2] = 0
    if t == 3:
        board[p+1][q] = board[p+2][q] = board[p+2][q+1] = 0
    if t == 4:
        board[p][q+1] = board[p-1][q+1] = board[p-2][q+1] = 0
    if t == 5:
        board[p][q+1] = board[p-1][q+1] = board[p][q+2] = 0

def solution(board):
    answer = 0
    while True:
        findSet = set()
        noRemove = True
        for j in range(len(board)):
            for i in range(len(board)):
                if board[i][j] != 0 and board[i][j] not in findSet:
                    findSet.add(board[i][j])
                    t = findType(board, i, j)
                    if isRemovable(board, i, j, t):
                        remove(board, i, j, t)
                        answer += 1
                        noRemove = False
                    break
        if noRemove:
            break
    # for row in board:
    #     print(row)
    return answer