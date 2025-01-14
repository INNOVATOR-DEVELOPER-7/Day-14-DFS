# Day-14-DFS
Here's Python Program for DFS (Depth First Search). Day 14 of Day 365.
- Initial Setup: Start with a graph, represented as nodes (vertices) and edges, and a starting node (source).
- Stack Initialization: Create a stack and push the starting node onto it. Mark the starting node as visited.
- Explore Nodes:
  - Pop a node from the stack.
  - Visit the node.
  - Push all its adjacent (neighboring) nodes that haven't been visited onto the stack.
  - Mark these adjacent nodes as visited.
- Repeat: Continue the process until the stack is empty.

Example:
Graph:

```
A - B - C
|   |
D - E - F
|       |
G - H - I
```

Starting Node: A

1. Initial Stack: [A]
2. Pop A, visit neighbors: B, D (push B and D onto the stack)
   - Stack: [B, D]
3. Pop D, visit neighbors: G (push G onto the stack)
   - Stack: [B, G]
4. Pop G, visit neighbors: H (push H onto the stack)
   - Stack: [B, H]
5. Pop H, no new neighbors.
   - Stack: [B]
6. Pop B, visit neighbors: C, E (push C and E onto the stack)
   - Stack: [C, E]
7. Pop E, visit neighbors: F (push F onto the stack)
   - Stack: [C, F]
8. Pop F, visit neighbors: I (push I onto the stack)
   - Stack: [C, I]
9. Pop I, no new neighbors.
   - Stack: [C]
10. Pop C, no new neighbors.
    - Stack: [ ] (empty, search complete)

Traversal Order: A, D, G, H, B, E, F, I, C
