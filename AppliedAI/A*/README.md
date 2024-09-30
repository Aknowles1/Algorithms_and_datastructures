A* Search Algorithm
Introduction

A* (A-star) is a search algorithm used to find the shortest path in graphs. It is widely used in navigation, games, and robotics. A* efficiently combines the strengths of Dijkstra's Algorithm (which guarantees the shortest path) and Greedy Best-First Search (which focuses on exploration toward the goal).
Algorithm Details

A* works by evaluating two factors:

    g(n): The exact cost of the path from the starting node to the current node.
    h(n): A heuristic estimate of the cost from the current node to the goal. This function is designed to guide the search toward the goal.

Common Heuristics

    Manhattan Distance: Used for grid-based navigation (no diagonal movement).
    Euclidean Distance: Used when diagonal movement is allowed.

The algorithm expands nodes based on their f(n) value, which is the sum of g(n) and h(n):
f(n)=g(n)+h(n)
f(n)=g(n)+h(n)

The algorithm uses a priority queue (usually implemented as a min-heap) to expand the node with the lowest f(n).
How It Works

    Start with the initial node, add it to the open list.
    Expand the node with the lowest f(n) from the open list.
    For each neighbor of the current node:
        Calculate g, h, and f values.
        If the neighbor is not in the open list, add it.
        If the neighbor is already in the open list but with a higher f, skip it.
    Repeat until the goal is reached or the open list is empty.

Code Explanation

The Python code implementation does the following:

    Defines a Node class that holds the position, g, h, and f values, as well as the parent for reconstructing the path.
    Uses a priority queue (via heapq) to store nodes to be explored, ensuring that the node with the lowest f value is explored first.
    Implements a simple 4-direction movement on a 2D grid, where 0 represents open space and 1 represents obstacles.
    The path is reconstructed by tracing back the parent pointers from the goal to the start node.

Heuristic Function

The heuristic function is critical in determining how A* navigates the search space. In our example, we use the Manhattan distance, which is appropriate for a grid where movement is restricted to horizontal and vertical directions.
Complexity

    Time complexity: O(b^d), where b is the branching factor (number of neighbors) and d is the depth of the solution. However, with a good heuristic, the search can be significantly faster.
    Space complexity: O(b^d) because of the storage needed for the open and closed lists.

Example

python

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

