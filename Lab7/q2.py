def heuristic(n):
    H_dist = {
        'S': 5,
        'A': 7,
        'B': 3,
        'C': 4,
        'D': 6,
        'E': 5,
        'F': 6,
        'G10': 10,
        'G20': 20,
        'G30': 30
    }
    return H_dist[n]

Graph_nodes = {
    'S': [('A', 5), ('D', 6), ('C', 6)],
    'A': [('S', 5), ('B', 9), ('G10', 9)],
    'B': [('A', 9), ('C', 1)],
    'C': [('B', 1), ('S', 6), ('F', 7), ('G20', 5)],
    'D': [('S', 6), ('E', 2)],
    'E': [('D', 2), ('G30', 7)],
    'F': [('C', 7), ('G30', 8)],
    'G10': [],
    'G20': [],
    'G30': []
}

def aStarAlgo(start, goals):
    open_set = set([start])
    closed_set = set()
    g = {start: 0}
    parents = {start: start}
    
    while open_set:
        n = min(open_set, key=lambda x: g[x] + heuristic(x))
        
        if n in goals:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start)
            path.reverse()
            print("Path:", " -> ".join(path))
            return
        
        open_set.remove(n)
        closed_set.add(n)
        
        for m, weight in Graph_nodes.get(n, []):
            if m in closed_set:
                continue
            if m not in open_set:
                open_set.add(m)
                parents[m] = n
                g[m] = g[n] + weight
            elif g[m] > g[n] + weight:
                g[m] = g[n] + weight
                parents[m] = n
                
    print("Path does not exist")

goal_nodes = ['G10', 'G20', 'G30']
aStarAlgo('S', goal_nodes)
