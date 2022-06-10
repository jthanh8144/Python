import heapq
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

class Node:
    COST = '__COST__'
    GOAL_COST = '__GOAL_COST__'
    A_STAR = '__A_STAR__'

    def __init__(self, label, cost=100000, goal_cost=100000):
        self.label = label
        self.cost = cost 
        self.goal_cost = goal_cost 
        self.compare_mode = Node.COST  
        self.path = []
        self.parents = []
        self.children = []
        self.depth = 0

    def __repr__(self):
        return str(dict({
            "label": self.label,
            "cost": self.cost,
            "goal_cost": self.goal_cost,
        }))

    def __hash__(self):
        return hash(self.label)

    def __eq__(self, other):
        return self.label == other.label

    def __lt__(self, other):
        if self.compare_mode is Node.COST:
            return self.cost < other.cost
        if self.compare_mode is Node.GOAL_COST:
            return self.goal_cost < other.goal_cost
        if self.compare_mode is Node.A_STAR:
            return self.cost + self.goal_cost < other.cost + other.goal_cost
        return self.cost < other.cost

    def get_label(self):
        return self.label

    def get_children(self):
        return [node.get_label() for node in self.children]

    def get_parents(self):
        return [node.get_label() for node in self.parents]

    def get_neighbors(self):
        return [node.get_label() for node in self.neighbors()]

    def neighbors(self):
        children = self.children
        parents = self.parents
        neigbors = children + parents
        seen = set()
        neigbors = [x for x in children + parents if not (x in seen or seen.add(x))]
        return neigbors

    def set_compare_mode(self, mode):
        if mode != Node.COST and mode != Node.A_STAR and mode != Node.GOAL_COST:
            self.compare_mode = Node.COST
        else:
            self.compare_mode = mode

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def clear(self):
        self.nodes = []
        self.edges = []

    def number_of_nodes(self):
        return len(self.nodes)

    def number_of_edges(self):
        return len(self.edges)

    def get_index(self, node):
        for idx, n in enumerate(self.nodes):
            if n == node:
                return idx
        return -1

    def is_contains(self, node):
        for el in self.nodes:
            if el == node:
                return True
        return False

    def add_node(self, label):
        node = Node(label)
        if not self.is_contains(node):
            self.nodes.append(node)

    def add_node_from(self, array_of_label):
        for el in array_of_label:
            self.add_node(label=el)

    def add_edge(self, start_label, end_label, weight=10000):
        start_node = Node(start_label)
        end_node = Node(end_label)
        if not self.is_contains(start_node):
            self.add_node(start_node)
        if not self.is_contains(end_node):
            self.add_node(end_node)
        start_index = self.get_index(start_node)
        end_index = self.get_index(end_node)
        self.nodes[start_index].children.append(self.nodes[end_index])
        self.nodes[end_index].parents.append(self.nodes[start_index])
        self.edges.append((self.nodes[start_index], self.nodes[end_index], weight))

    def add_edges_from(self, array_of_tuple_node, is_duplicated=False):
        for tup in array_of_tuple_node:
            start = tup[0]
            end = tup[1]
            if len(tup) == 3:
                weight = tup[2] or 10000
            else:
                weight = 10000
            self.add_edge(start, end, weight)
            if is_duplicated:
                self.add_edge(end, start, weight)

    def get_edge(self, start_node, end_node):
        try:
            return [edges for edges in self.edges if edges[0] == start_node
                    and edges[1] == end_node][0]
        except:
            return None

    def show_nodes(self):
        return [node.get_label() for node in self.nodes]

    def show_edges(self):
        return [(edge[0].get_label(), edge[1].get_label(), edge[2]) for edge in self.edges]

    def set_compare_mode(self, mode):
        for node in self.nodes:
            node.set_compare_mode(mode)

def update_cost(g, current_node, prev_node):
    if g.get_edge(prev_node, current_node) is not None:
        if current_node.cost > prev_node.cost + graph.get_edge(prev_node, current_node)[2]:
            current_node.cost = prev_node.cost + graph.get_edge(prev_node, current_node)[2]
            current_node.path = prev_node.path + [current_node.get_label()]


def find_by_label(array_of_node, node):
    for idx, n in enumerate(array_of_node):
        if n == node:
            return idx
    return -1


def update_frontier(frontier, new_node):
    index = find_by_label(frontier, new_node)
    if index >= 0:
        if frontier[index] > new_node:
            frontier[index] = new_node

def A_star(initial_state, goalTest):
    frontier = list()
    explored = list()
    heapq.heapify(frontier)
    heapq.heappush(frontier, initial_state)
    df = pd.DataFrame(columns=["Frontier", "Explored"])
    pd.set_option("max_colwidth", None)
    while len(frontier) > 0:
        to_append = [
            list(map(lambda x: x.get_label(), frontier)),
            list(map(lambda x: x.get_label(), explored))
        ]
        series = pd.Series(to_append, index=df.columns)
        df = df.append(series, ignore_index=True)
        state = heapq.heappop(frontier)
        explored.append(state)
        if state == goalTest:
            print(df)
            return True
        for neighbor in state.neighbors():
            update_cost(graph, current_node=neighbor, prev_node=state)
            if neighbor.get_label() not in list(set([node.get_label() for node in frontier + explored])):
                heapq.heappush(frontier, neighbor)
            elif find_by_label(array_of_node=frontier, node=neighbor) >= 0:
                update_frontier(frontier=frontier, new_node=neighbor)
    return False


V = [('S', 10), ('A', 9), ('B', 8), ('C', 7), ('D', 6), ('E', 5), ('F', 4), ('G', 10),
     ('H', 10), ('K', 3), ('M', 0), ('N', 10), ('I', 6), ('J', 0), ('L', 9), ('Z', 8)]
E = [('S', 'A', 5), ('S', 'B', 6), ('S', 'C', 6), ('A', 'D', 6),
     ('A', 'E', 7), ('B', 'F', 3), ('B', 'G', 4), ('C', 'H', 6),
     ('C', 'K', 4), ('D', 'M', 5), ('D', 'N', 8), ('E', 'I', 8),
     ('F', 'J', 4), ('K', 'Z', 8)]

graph = Graph()
graph.add_node_from([i[0] for i in V])
graph.add_edges_from(E)
print(graph.nodes[0])

for i in range(len(V)):
    graph.nodes[i].goal_cost = V[i][1]

graph.nodes[0].cost = 0 
graph.set_compare_mode(Node.A_STAR)

for i in range(len(V)):
    if (V[i][1] == 0):
        A_star(initial_state=graph.nodes[0], goalTest=graph.nodes[i])