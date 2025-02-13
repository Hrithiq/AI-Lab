graph = {
    'M': {'T': 8},
    'T': {'F': 3, 'C': 29},
    'F': {'M': 11, 'B': 46},
    'C': {'M': 40, 'H': 17},
    'H': {'T': 31, 'B': 40, 'D': 53},
    'B': {'D': 15},
    'D': {'B': 17}
}

def uniform_cost_search(graph, start, goal):
    queue = [(0, start, [])]
    visited = {}

    while queue:
        queue.sort()
        cost, node, path = queue.pop(0)

        if node in visited and visited[node] <= cost:
            continue
        visited[node] = cost
        path = path + [node]

        if node == goal:
            return path, cost

        for neighbor in graph[node]:
            queue.append((cost + graph[node][neighbor], neighbor, path))

path, cost = uniform_cost_search(graph, 'M', 'D')
print("Shortest path:", path, "with cost =", cost)
