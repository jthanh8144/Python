def Check(O):
    if O[0] > 0 and O[0] < O[1]:
        return False
    if O[3] > 0 and O[3] < O[4]:
        return False
    return True

def Children(O):
    res = []
    # 1. 2 người qua sông
    if O[2] == 0:
        if O[0] >= 2:
            child = [O[0] - 2, O[1], 1, O[3] + 2, O[4]]
            if Check(child):
                res.append(child)
    else:
        if O[3] >= 2:
            child = [O[0] + 2, O[1], 0, O[3] - 2, O[4]]
            if Check(child):
                res.append(child)
    # 2. 2 quỷ qua sông
    if O[2] == 0:
        if O[1] >= 2:
            child = [O[0], O[1] - 2, 1, O[3], O[4] + 2]
            if Check(child):
                res.append(child)
    else:
        if O[4] >= 2:
            child = [O[0], O[1] + 2, 0, O[3], O[4] - 2]
            if Check(child):
                res.append(child)
    # 3. 1 người qua sông
    if O[2] == 0:
        if O[0] >= 1:
            child = [O[0] - 1, O[1], 1, O[3] + 1, O[4]]
            if Check(child):
                res.append(child)
    else:
        if O[3] >= 1:
            child = [O[0] + 1, O[1], 0, O[3] - 1, O[4]]
            if Check(child):
                res.append(child)
    # 4. 1 quỷ qua sông
    if O[2] == 0:
        if O[1] >= 1:
            child = [O[0], O[1] - 1, 1, O[3], O[4] + 1]
            if Check(child):
                res.append(child)
    else:
        if O[4] >= 1:
            child = [O[0], O[1] + 1, 0, O[3], O[4] - 1]
            if Check(child):
                res.append(child)
    # 5. 1 người 1 quỷ qua sông
    if O[2] == 0:
        if O[0] >= 1 and O[1] >= 1:
            child = [O[0] - 1, O[1] - 1, 1, O[3] + 1, O[4] + 1]
            if Check(child):
                res.append(child)
    else:
        if O[3] >= 1 and O[4] >= 1:
            child = [O[0] + 1, O[1] + 1, 0, O[3] - 1, O[4] - 1]
            if Check(child):
                res.append(child)
    return res

# Số người bên trái, số quỷ bên trái, vị trí thuyền, số người bên phải, số quỷ bên phải
start = [3, 3, 0, 0, 0]
goal = [0, 0, 1, 3, 3]

OK = False

# B1:
open = [(start, None)]
closed = []
# B2:
# B6:
while len (open):
    # B3
    # BFS:
    # O_TT = open.pop(0)
    # DFS:
    O_TT = open.pop()
    O = O_TT[0]
    closed.append(O)
    # B4
    if O == goal:
        OK = True
        break
    # B5
    for child in Children(O):
        if child not in open and child not in closed:
            open.append((child, O_TT))

print(OK)
print(O_TT)
