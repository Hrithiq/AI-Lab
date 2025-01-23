maze = {
    1: [6, 2],
    2: [1, 3],
    3: [8, 2],
    4: [5],
    5: [10, 4],
    6: [1, 11],
    7: [8],
    8: [3, 7],
    9: [14, 10],
    10: [5, 15, 9],
    11: [6, 12],
    12: [17, 11],
    13: [14],
    14: [9, 19, 13],
    15: [10, 20],
    16: [17],
    17: [12, 16, 18],
    18: [17, 19],
    19: [14, 18],
    20: [15],
}


def dfs(maze, current, goal, visited, path):
    if current == goal:
        path.append(current)
        return True

    visited.add(current) 
    path.append(current)  

    for neighbor in maze[current]:
        if neighbor not in visited:
            if dfs(maze, neighbor, goal, visited, path):
                return True

    path.pop() 
    return False


start = 2  
goal = 20 
visited = set()
path = []

if dfs(maze, start, goal, visited, path):
    print("Path to exit the maze:")
    for node in path:
        print(node)
else:
    print("No path found.")


# Output:

# 2
# 1
# 6
# 11
# 12
# 17
# 16
# 18
# 19
# 14
# 9
# 10
# 15
# 20