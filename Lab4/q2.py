graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
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

count = 0
while len(queue) > 0:
    node = queue[0]
    queue = queue[1:]
    count += 1
    
    for neighbor in graph[node]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            queue.append(neighbor)

if count == len(graph):
    print("No Cycle")
else:
    print("Cycle Detected")
