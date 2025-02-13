graph = {
    'S': {'1': 2, '3': 5},
    '1': {'G': 1},
    '2': {'1': 4},
    '3': {'1': 5, '4': 2, 'G': 6},
    '4': {'2': 4, '5': 3},
    '5': {'2': 6, 'G': 3},
    'G': {'4': 7}
}

def uniform_cost_search(graph, start, goal):
    queue = [(0, start)]
    visited = {}

    while len(queue) > 0:
        queue.sort()
        cost, node = queue[0]
        queue = queue[1:]

        if node in visited:
            continue
        visited[node] = cost

        if node == goal:
            return cost

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((cost + graph[node][neighbor], neighbor))

cost = uniform_cost_search(graph, 'S', 'G')
print("Minimum cost from S to G is =", cost)
