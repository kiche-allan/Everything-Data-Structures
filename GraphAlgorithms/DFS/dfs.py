def dfs(graph, start):
    visited = set()
    stack = [ start]
    while stack:
        node = stack.pop()
        if node is not visited:
            visited.add(node)
            print(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    stack.append(neighbour)
        
# Line 1: The dfs() function takes two arguments: the graph and the start node. The graph is a dictionary that maps nodes to their adjacent nodes. The start node is the node that the search will start at.

# Line 2: The visited set is used to keep track of the nodes that have been visited. The stack list is used to keep track of the nodes that have been visited but not yet fully explored.

# Line 3: The while loop iterates until the stack is empty. In each iteration, the code pops the top node off the stack, marks it as visited, and prints it. It then adds all of the node's adjacent nodes to the stack that have not been visited yet.

# Line 4: The if node not in visited: statement checks if the node has already been visited. If it has not been visited, the code marks it as visited and prints it.

# Line 5: The for neighbor in graph[node]: statement iterates through the node's adjacent nodes. If a neighbor has not been visited yet, the code appends it to the stack.

# Line 6: The return None statement returns None, which indicates that the function has completed successfully.

# I hope this explanation was helpful. Let me know if you have any other questions.