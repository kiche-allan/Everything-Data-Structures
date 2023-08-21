from collections import deque

def bfs(graph, source):
    visited = set()
    queue = deque()

    queue.append(source)
    visited.add(source)

    while queue:
        current_node = queue.popleft()

        #process the current node here

        for neighbour in graph[current_node]:
            if neighbour not in visited:
                queue. append(neighbour)
                visited.add(neighbour)

    #example usage
    #assuming the graph is represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
}