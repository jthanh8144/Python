def move(s, E):
    result = []
    for item in E:
        if item[0] == s:
            result.append(item)
    return result

V = ["a", "b", "c", "d", "e", "f"]
E = [("a", "d"),
     ("a", "f"),
     ("d", "f"),
     ("d", "a"),
     ("d", "c"),
     ("f", "d"),
     ("f", "a"),
     ("c", "c"),
     ("c", "b"),
     ("c", "e"),
     ("c", "d"),
     ("e", "c"),
     ("b", "c"),]
start = "a"
Goal = "b"
OK = False
Open = [(start, None)]
Closed = []

while len(Open) > 0:
    O_TT = Open.pop()
    O = O_TT[0]
    if O == Goal:
        OK = True
        break
    for i in move(O, E):
        if i not in Closed and i not in Open:
            Open.append((i[1], O_TT))
            Closed.append(i)

print(O_TT)