import random

def positionZero(S):
    n = len(S)
    for i in range(n):
        for j in range(n):
            if S[i][j] == 0:
                return i,j 

# O = 0: Up
# O = 1: Down
# O = 2: Left
# O = 3: Right
def move(S, O):
    L = [list(x) for x in S]
    i, j = positionZero(S)
    if O == 0:
        if i < 2:
            L[i][j] = L[i + 1][j]
            L[i + 1][j] = 0
            return tuple([tuple(x) for x in L])
    elif O == 1:
        if i > 0:
            L[i][j] = L[i - 1][j]
            L[i - 1][j] = 0
            return tuple([tuple(x) for x in L])
    elif O == 2:
        if j < 2:
            L[i][j] = L[i][j + 1]
            L[i][j + 1] = 0
            return tuple([tuple(x) for x in L])
    elif O == 3:
        if j > 0:
            L[i][j] = L[i][j - 1]
            L[i][j - 1] = 0
            return tuple([tuple(x) for x in L])
    return None
    

# Số người bên trái, số quỷ bên trái, vị trí thuyền, số người bên phải, số quỷ bên phải
goal = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
start = goal
for _ in range(500):
    O = move(start, random.randint(0, 3))
    if O != None:
        start = O

for _ in start:
    print(_)

OK = False

# B1:
open = [(start, None, None)]
closed = {start}
# B2:
# B6:
while len(open) > 0:
    # B3
    # BFS:
    O_TT = open.pop(0)
    O = O_TT[0]
    # B4
    if O == goal:
        OK = True
        break
    # B5
    for i in range(4):
        child = move(O, i)
        if child != None and child not in closed:
            open.append((child, i, O_TT))
            closed.add(child)

print(OK)

def PrintOTT(O_TT):
    if O_TT[2] != None:
        PrintOTT(O_TT[2])
        print(O_TT[1])
    for _ in O_TT[0]:
        print(_)

PrintOTT(O_TT)
