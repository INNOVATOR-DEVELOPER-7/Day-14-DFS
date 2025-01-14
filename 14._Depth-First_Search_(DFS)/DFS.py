def dfs(graph, start_node, visited=None):
    if visited is None:
        visited = set()
    visited.add(start_node)
    
    # Process the current node (print it)
    print(start_node, end=" ")
    
    # Recur for all the adjacent nodes that have not been visited
    for neighbor in graph[start_node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Get the graph from the user
user_input = input("Enter the graph as adjacency list (e.g., {'A': ['B', 'C'], 'B': ['A', 'D'], ...}): ")
graph = eval(user_input)

# Get the starting node from the user
start_node = input("Enter the starting node: ")

# Perform DFS
print("Depth-First Search starting from node", start_node, ":")
dfs(graph, start_node)
