class PuzzleNode:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f

def misplaced_tiles(state, goal):
    return sum(1 for i in range(3) for j in range(3) if state[i][j] and state[i][j] != goal[i][j])

def get_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def generate_neighbors(node, goal):
    x, y = get_blank_position(node.state)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []

    for dx, dy in moves:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in node.state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            h = misplaced_tiles(new_state, goal)
            neighbors.append(PuzzleNode(new_state, node, node.g + 1, h))

    return neighbors

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]

def a_star(initial_state, goal_state):
    open_list = []
    closed_set = set()
    
    initial_h = misplaced_tiles(initial_state, goal_state)
    start_node = PuzzleNode(initial_state, g=0, h=initial_h)
    
    open_list.append(start_node)

    while open_list:
        open_list.sort()
        current_node = open_list.pop(0)

        if current_node.state == goal_state:
            return reconstruct_path(current_node)

        closed_set.add(tuple(map(tuple, current_node.state)))

        for neighbor in generate_neighbors(current_node, goal_state):
            if tuple(map(tuple, neighbor.state)) in closed_set:
                continue
            open_list.append(neighbor)

    return None

def print_puzzle(state):
    for row in state:
        print(" ".join(str(x) if x != 0 else " " for x in row))
    print()

initial_state = [[2, 8, 3], [1, 6, 4], [7, 0, 5]]
goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

solution_path = a_star(initial_state, goal_state)

if solution_path:
    for step in solution_path:
        print_puzzle(step)
else:
    print("No solution exists.")
