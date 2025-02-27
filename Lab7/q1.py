def heuristic(n):
    H_dist = {
        'A': 10,
        'B': 8,
        'C': 5,
        'D': 7,
        'E': 3,
        'F': 6,
        'G': 5,
        'H': 3,
        'I': 1,
        'J': 0
    }
    return H_dist[n]

Graph_nodes = {
    'A': [('B', 6), ('F', 3)],
    'B': [('A', 6), ('C', 3), ('D', 2)],
    'C': [('B', 3), ('E', 5)],
    'D': [('B', 2), ('E', 8), ('G', 7)],
    'E': [('C', 5), ('D', 8), ('J', 5)],
    'F': [('A', 3), ('G', 1)],
    'G': [('D', 7), ('F', 1), ('I', 3)],
    'H': [('I', 2), ('J', 3)],
    'I': [('G', 3), ('H', 2), ('J', 1)],
    'J': [('E', 5), ('I', 1), ('H', 3)]
}

def aStarAlgo(start, stop):
    open_set = set([start])
    closed_set = set()
    g = {start: 0}
    parents = {start: start}
    
    while open_set:
        n = min(open_set, key=lambda x: g[x] + heuristic(x))
        
        if n == stop:
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

aStarAlgo('A', 'J')
