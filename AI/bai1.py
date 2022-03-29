
V = ["a", "b", "c", "d", "e", "f"]
E = [("a", "d"),
     ("d", "a"),
     ("a", "f"),
     ("f", "a"),
     ("d", "f"),
     ("f", "d"),
     ("d", "c"),
     ("c", "d"),
     ("c", "c"),
     ("c", "e"),
     ("e", "c"),
     ("b", "c"),
     ("c", "b"), ]


def gen_graph(V, E):
    result = {V[i]: [] for i in range(len(V))}
    for node in result:
        for child in E:
            if (child[0] == node):
                result[child[0]].append(child[1])
    return result


def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = []
    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            if vertex == goal:
                return path
            visited.append(vertex)
            for neighbor in graph[vertex]:
                stack.append((neighbor, path + [neighbor]))


solution = dfs(gen_graph(V, E), 'a', 'b')
if solution:
    n = len(solution)
    for i in range(n - 1):
        print(solution[i], end=' -> ')
    print(solution[n - 1])
else:
    print('Không tìm thấy đường đi')
