graph = {
    'A': {'B': 2, 'C': 3, 'D': 1},
    'B': {'A': 2, 'C': 4, 'D': 2},
    'C': {'A': 3, 'B': 4, 'D': 3},
    'D': {'A': 1, 'B': 2, 'C': 3}
}

def bfs_tsp(graph, start):
    queue = [(start, [start], 0)]
    min_cost = float('inf')
    best_path = []
    
    while len(queue) > 0:
        node, path, cost = queue[0]
        queue = queue[1:]
        
        if len(path) == len(graph):
            total_cost = cost + graph[node][start]
            if total_cost < min_cost:
                min_cost = total_cost
                best_path = path + [start]
        
        for neighbor in graph[node]:
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor], cost + graph[node][neighbor]))

    return best_path, min_cost

path, cost = bfs_tsp(graph, 'A')
print(path, cost)
