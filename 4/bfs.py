def bfs(graph, start):
    visited = set()
    queue = []  # Initialize the queue (list)

    # Step 2: Add the start node to the queue and mark it as visited
    # Your code here

    while queue:
        # Step 3: Dequeue a vertex from the queue
        # Your code here

        # Step 3: Print the current node
        # Your code here

        # Step 3: Get all adjacent vertices of the dequeued vertex
        # If an adjacent vertex has not been visited, mark it visited and enqueue it
        # Your code here

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Start BFS from node 'A'
print("BFS Traversal starting from node A:")
# Call your BFS function here
