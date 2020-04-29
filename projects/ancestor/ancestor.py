class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

def earliest_ancestor(ancestors, starting_node):
    graph = {}

    def build_graph(pair):
        vertex = pair[1]
        edge = pair[0]

        if vertex not in graph:
            graph[vertex] = set()
        graph[vertex].add(edge)

    def get_nieghbors(vertex):
        if vertex in graph:
            return graph[vertex]
        else:
            return None

    for pair in ancestors:
        build_graph(pair)

    Next_ancestor = Stack()
    earliest_ancestor = [starting_node]
    Next_ancestor.push([starting_node])

    while Next_ancestor.size() > 0:
        current_ancestor_path = Next_ancestor.pop()
        current_ancestor = current_ancestor_path[-1]

        if len(current_ancestor_path) > len(earliest_ancestor):
            earliest_ancestor = current_ancestor_path

        elif len(current_ancestor_path) == len(earliest_ancestor):
            if current_ancestor_path[-1] < earliest_ancestor[-1]:
                earliest_ancestor = current_ancestor_path

        if get_nieghbors(current_ancestor):
            for neighbor in get_nieghbors(current_ancestor):
                ancestor_tree = list(current_ancestor_path)
                next_ancestor_tree = ancestor_tree + [neighbor]

                Next_ancestor.push(next_ancestor_tree)

    print("Ancestor Tree", earliest_ancestor)
    print("Earliest Ancestor", earliest_ancestor[-1])

    if earliest_ancestor[-1] == starting_node:
        return -1
    else:
        return earliest_ancestor[-1]

    