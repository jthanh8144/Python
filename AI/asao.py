from opcode import opname
import random
from queue import PriorityQueue

def positionZero(S):
    n = len(S)
    for i in range(n):
        for j in range(n):
            if S[i][j] == 0:
                return i, j

# O = 0: Up
# O = 1: Down
# O = 2: Left
# O = 3: Right

def move(S, O, n):
    L = [list(x) for x in S]
    i, j = positionZero(S)
    if O == 0:
        if i < n - 1:
            L[i][j] = L[i + 1][j]
            L[i + 1][j] = 0
            return tuple([tuple(x) for x in L])
    elif O == 1:
        if i > 0:
            L[i][j] = L[i - 1][j]
            L[i - 1][j] = 0
            return tuple([tuple(x) for x in L])
    elif O == 2:
        if j < n - 1:
            L[i][j] = L[i][j + 1]
            L[i][j + 1] = 0
            return tuple([tuple(x) for x in L])
    elif O == 3:
        if j > 0:
            L[i][j] = L[i][j - 1]
            L[i][j - 1] = 0
            return tuple([tuple(x) for x in L])
    return None

def distance(A, B):
    n = len(A)
    d = 0
    for i in range(n):
        for j in range(n):
            if A[i][j] != 0 and A[i][j] != B[i][j]:
                d += 1
    return d

n = 5
# goal = ((1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12), (13, 14, 15, 0))
goal = tuple([tuple([(i*5 + j+1)%25 for j in range(5)]) for i in range(5)])
print(goal)
start = goal
for _ in range(5000):
    O = move(start, random.randint(0, 3), n)
    if O != None:
        start = O

for _ in start:
    print(_)

OK = False

# B1:
# open = [(start, None, None)]
open = PriorityQueue()
open.put(((0, 0), start, None, None))
closed = {start}

count = 0
# B2:
# B6:
while not open.empty():
    count += 1
    # B3
    # BFS:
    O_TT = open.get()
    O = O_TT[1]
    # B4
    if O == goal:
        OK = True
        break
    # B5
    for i in range(4):
        child = move(O, i, n)
        if child != None and child not in closed:
            g = O_TT[0][1] + 1
            h = distance(child, goal)
            f = g + h
            open.put(((h, g), child, i, O_TT))
            closed.add(child)

print(OK)


def PrintOTT(O_TT):
    if O_TT[3] != None:
        PrintOTT(O_TT[3])
        print(O_TT[2])
    for _ in O_TT[1]:
        print(_)


PrintOTT(O_TT)
print(OK, count)
