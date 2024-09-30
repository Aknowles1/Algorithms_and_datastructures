import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position  # (x, y) position on the grid
        self.parent = parent      # Parent node for path reconstruction
        self.g = 0                # Cost from start to current node
        self.h = 0                # Heuristic (estimated cost to goal)
        self.f = 0                # Total cost (f = g + h)

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f

def a_star_search(start, goal, grid):
    """
    A* algorithm to find the shortest path in a 2D grid.

    :param start: (x, y) tuple for the start position
    :param goal: (x, y) tuple for the goal position
    :param grid: 2D list where 0 represents open space and 1 represents obstacles
    :return: List of tuples representing the path from start to goal
    """
    # Create the start and goal nodes
    start_node = Node(start)
    goal_node = Node(goal)

    # Open list (priority queue) and closed list (visited nodes)
    open_list = []
    closed_list = set()

    # Add the start node to the open list
    heapq.heappush(open_list, start_node)

    # Loop until you find the goal
    while open_list:
        # Get the node with the lowest f score
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)

        # Check if we have reached the goal
        if current_node == goal_node:
            return reconstruct_path(current_node)

        # Generate neighbors (up, down, left, right, diagonal)
        neighbors = get_neighbors(current_node, grid)

        for neighbor_pos in neighbors:
            if neighbor_pos in closed_list:
                continue

            # Create a neighbor node
            neighbor_node = Node(neighbor_pos, current_node)

            # Calculate the g, h, and f values
            neighbor_node.g = current_node.g + 1  # Each move has a cost of 1
            neighbor_node.h = heuristic(neighbor_node.position, goal_node.position)
            neighbor_node.f = neighbor_node.g + neighbor_node.h

            # If the neighbor is already in the open list with a lower f value, skip it
            if any(neighbor.position == neighbor_node.position and neighbor.f < neighbor_node.f for neighbor in open_list):
                continue

            # Otherwise, add the neighbor to the open list
            heapq.heappush(open_list, neighbor_node)

    # If we exit the loop without finding a path, return None
    return None

def reconstruct_path(current_node):
    """
    Reconstruct the path from the goal node to the start node by following parent pointers.
    
    :param current_node: The goal node
    :return: List of tuples representing the path
    """
    path = []
    while current_node is not None:
        path.append(current_node.position)
        current_node = current_node.parent
    return path[::-1]  # Return reversed path (from start to goal)

def get_neighbors(node, grid):
    """
    Generate the valid neighbors for the current node (4 possible directions).
    
    :param node: The current node
    :param grid: 2D grid representing the environment
    :return: List of valid neighbor positions
    """
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, down, left, right

    for direction in directions:
        neighbor_pos = (node.position[0] + direction[0], node.position[1] + direction[1])

        # Check if the neighbor is within bounds and not an obstacle
        if 0 <= neighbor_pos[0] < len(grid) and 0 <= neighbor_pos[1] < len(grid[0]) and grid[neighbor_pos[0]][neighbor_pos[1]] == 0:
            neighbors.append(neighbor_pos)

    return neighbors

def heuristic(position, goal):
    """
    Heuristic function that estimates the distance from the current node to the goal.
    Using Manhattan distance (for grid-based movement).
    
    :param position: Current node position (x, y)
    :param goal: Goal node position (x, y)
    :return: Estimated cost to reach the goal
    """
    return abs(position[0] - goal[0]) + abs(position[1] - goal[1])

# Example Usage
if __name__ == "__main__":
    # Example 5x5 grid (0: open space, 1: obstacle)
    grid = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
    ]

    start = (0, 0)  # Starting point
    goal = (4, 4)   # Goal point

    path = a_star_search(start, goal, grid)

    if path:
        print("Path found:", path)
    else:
        print("No path found.")
