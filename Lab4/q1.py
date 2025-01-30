graph = {
    5: [2, 0],
    4: [1, 0],
    2: [3],
    3: [1],
    1: [],
    0: []
}

in_degree = {}
for node in graph:
    in_degree[node] = 0
for node in graph:
    for neighbor in graph[node]:
        in_degree[neighbor] += 1

queue = []
for node in in_degree:
    if in_degree[node] == 0:
        queue.append(node)

topo_sort = []
while len(queue) > 0:
    node = queue[0]
    queue = queue[1:]
    topo_sort.append(node)
    
    for neighbor in graph[node]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            queue.append(neighbor)

print(" ".join(map(str, topo_sort)))
