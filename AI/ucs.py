
V = ["a", "b", "c", "d", "e", "f"]
E = [("a", "b", 3),
     ("a", "d", 4),
     ("a", "f", 5),
     ("b", "c", 1),
     ("b", "f", 1),
     ("c", "d", 2),
     ("d", "b", 3),
     ("e", "d", 3),
     ("e", "f", 2),
     ("f", "d", 2)]

def gen_graph(V, E):
    result = {V[i]: [] for i in range(len(V))}
    for node in result:
        for child in E:
            if (child[0] == node):
                result[child[0]].append((child[1], child[2]))
    return result

def path_cost(path):
    total_cost = 0
    for (node, cost) in path:
        total_cost += cost
    return total_cost, path[-1][0]

def ucs(graph, start, goal):
    visited = []
    queue = [[(start, 0)]]
    while queue:
        queue.sort(key=path_cost)
        path = queue.pop(0)
        node = path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path
        else:
            adjacent_nodes = graph.get(node, [])
            for (node2, cost) in adjacent_nodes:
                new_path = path.copy()
                new_path.append((node2, cost))
                queue.append(new_path)

solution = ucs(gen_graph(V, E), 'c', 'f')
if solution:
    n = len(solution)
    for i in range(n - 1):
        print(solution[i][0], end=' -> ')
    print(solution[n - 1][0])
    print('Chi phí: ', path_cost(solution)[0])
else:
    print('Không tìm thấy đường đi')