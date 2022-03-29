
def isFinish(b):
    if b[0][0] == b[1][1] and b[0][0] == b[2][2] and b[0][0] != 0:
        return b[0][0]
    if b[2][0] == b[1][1] and b[2][0] == b[0][2] and b[2][0] != 0:
        return b[2][0]
    for i in range(3):
        if b[i][0] == b[i][1] and b[i][0] == b[i][2] and b[i][0] != 0:
            return b[i][0]
        if b[0][i] == b[1][i] and b[0][i] == b[2][i] and b[0][i] != 0:
            return b[0][i]
    for i in range(3):
        for j in range(3):
            if b[i][j] == 0:
                return -1
    return 0


def choiceBestMove(b, CPU, Player, depth):
    td = []
    for i in range(3):
        for j in range(3):
            if b[i][j] == 0:
                td.append((i, j))
    Max = -10
    tdMax = td[0]
    for i, j in td:
        child = [_[:] for _ in b]
        child[i][j] = CPU
        mm = minimax(child, depth, False, CPU, Player)
        if Max < mm:
            Max = mm
            tdMax = (i, j)
    return tdMax


def value(node, CPU):
    iF = isFinish(node)
    if iF == CPU:
        return 1
    elif iF <= 0:
        return 0
    else:
        return -1


def minimax(node, depth, mP, CPU, Player):
    if isFinish(node) > -1 or depth == 0:
        return value(node, CPU)
    if mP:
        Max = -10
        for i in range(3):
            for j in range(3):
                if node[i][j] == 0:
                    child = [_[:] for _ in node]
                    child[i][j] = CPU
                    Max = max(Max, minimax(
                        child, depth-1, not mP, CPU, Player))
        return Max
    else:
        Min = 10
        for i in range(3):
            for j in range(3):
                if node[i][j] == 0:
                    child = [_[:] for _ in node]
                    child[i][j] = Player
                    Min = min(Min, minimax(
                        child, depth-1, not mP, CPU, Player))
        return Min

def create_board(n):
    board = []
    for i in range(n):
        board.append([0]*n)
    return board

board = create_board(10)
for _ in board:
    print(_)

# CPU = 1
# Player = 2
# while True:
#     print("Choose the first player (CPU = 1, you = 2): ")
#     Now = int(input())
#     if (Now > 0 and Now < 3):
#         break

# while isFinish(board) == -1:
#     if Now == CPU:
#         print("CPU turn")
#         i, j = choiceBestMove(board, CPU, Player, 6)
#         board[i][j] = CPU
#         Now = Player
#     else:
#         print("Player turn")
#         while True:
#             i, j = map(int, input().split())
#             if board[i][j] == 0:
#                 board[i][j] = Player
#                 break
#         Now = CPU
#     for _ in board:
#         print(_)

# print("Finish")
# print(isFinish(board), "Won!!")
