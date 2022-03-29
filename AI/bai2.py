def checkVertical(posittion):
    x, y = posittion
    


def isFinish(b):
    return 0

def choiceBestMove(b, CPU, Player, depth):
    sz = len(b[0])
    td = []
    for i in range(sz):
        for j in range(sz):
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

def minimax(node, depth, mP, CPU, Player):
    if isFinish(node) > -1 or depth == 0:
        return value(node, CPU)
    if mP:
        Max = -10
        for i in range(10):
            for j in range(10):
                if node[i][j] == 0:
                    child = [_[:] for _ in node]
                    child[i][j] = CPU
                    Max = max(Max, minimax(
                        child, depth-1, not mP, CPU, Player))
        return Max
    else:
        Min = 10
        for i in range(10):
            for j in range(10):
                if node[i][j] == 0:
                    child = [_[:] for _ in node]
                    child[i][j] = Player
                    Min = min(Min, minimax(
                        child, depth-1, not mP, CPU, Player))
        return Min

def value(node, CPU):
    iF = isFinish(node)
    if iF == CPU:
        return 1
    elif iF <= 0:
        return 0
    else:
        return -1


def create_board(n):
    board = []
    for i in range(n):
        board.append([0]*n)
    return board


board = create_board(10)
for _ in board:
    print(_)
CPU = 1
Player = 2
while True:
    print("Choose the first player (CPU = 1, you = 2): ")
    Now = int(input())
    if (Now > 0 and Now < 3):
        break

while isFinish(board) == -1:
    if Now == CPU:
        print("CPU turn")
        i, j = choiceBestMove(board, CPU, Player, 6)
        board[i][j] = CPU
        Now = Player
    else:
        print("Player turn")
        while True:
            i, j = map(int, input().split())
            if board[i][j] == 0:
                board[i][j] = Player
                break
        Now = CPU
    for _ in board:
        print(_)

print("Finish")
print(isFinish(board), "Won!!")
