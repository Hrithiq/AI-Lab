graph = {
    'S': {'A': 5, 'B': 9, 'D': 6},
    'A': {'B': 3, 'G1': 9},
    'B': {'A': 2, 'C': 1},
    'C': {'S': 6, 'F': 7, 'G2': 5},
    'D': {'C': 2, 'E': 2},
    'E': {'G3': 7},
    'F': {'D': 2, 'G3': 8},
    'G1': {},
    'G2': {},
    'G3': {}
}

def uniform_cost_search(graph, start, goals):
    queue = [(0, start)]
    visited = {}

    while len(queue) > 0:
        queue.sort()
        cost, node = queue[0]
        queue = queue[1:]

        if node in visited:
            continue
        visited[node] = cost

        if node in goals:
            return node, cost

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((cost + graph[node][neighbor], neighbor))

goal, cost = uniform_cost_search(graph, 'S', {'G1', 'G2', 'G3'})
print("Goal node with least cost:", goal, "with cost =", cost)
