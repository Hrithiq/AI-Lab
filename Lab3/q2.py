class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_cycle(self, node, visited, rec_stack):
        visited[node] = True
        rec_stack[node] = True

        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                if self.dfs_cycle(neighbor, visited, rec_stack):
                    return True
            elif rec_stack[neighbor]:
                return True

        rec_stack[node] = False 
        return False

    def detect_cycle(self):
        visited = [False] * self.vertices
        rec_stack = [False] * self.vertices

        for node in range(self.vertices):
            if not visited[node]:
                if self.dfs_cycle(node, visited, rec_stack):
                    return True
        return False


g = Graph(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(2, 2) 
g.add_edge(3, 0)

# Check for cycles
if g.detect_cycle():
    print("Cycle detected in the graph.")
else:
    print("No cycle detected in the graph.")
