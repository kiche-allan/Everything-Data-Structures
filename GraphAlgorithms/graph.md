Graph algorithms are a set of techniques and methods used to solve problems that involve graphs. Graphs are mathematical structures that consist of vertices (also called nodes) and edges (also called links or arcs) that connect these vertices. Graphs are used to model a wide range of real-world phenomena, such as social networks, transportation systems, and computer networks.


There are many different types of graph algorithms, each designed to solve a particular class of problems. Some of the most common graph algorithms include:

Breadth-First Search (BFS): This algorithm is used to traverse a graph and visit all the nodes in a breadth-first manner. It can be used to find the shortest path between two nodes, or to detect cycles in a graph.

Depth-First Search (DFS): This algorithm is used to traverse a graph and visit all the nodes in a depth-first manner. It can be used to find connected components in a graph, or to detect cycles in a graph.

Dijkstra's Algorithm: This algorithm is used to find the shortest path between two nodes in a weighted graph. It works by maintaining a set of unvisited nodes and a set of tentative distances from the start node to each node in the graph.

Bellman-Ford Algorithm: This algorithm is used to find the shortest path between two nodes in a weighted graph, even when the graph contains negative weight edges. It works by iteratively relaxing the edges in the graph until no further improvements can be made.

An undirected graph is a graph in which the edges do not point in any direction (ie. the edges are bidirectional).

A connected graph is a graph in which there is always a path from a vertex to any other vertex.

Spanning tree
A spanning tree is a sub-graph of an undirected connected graph, which includes all the vertices of the graph with a minimum possible number of edges. If a vertex is missed, then it is not a spanning tree.

Prim's Algorithm: This algorithm is used to find the minimum spanning tree of a weighted graph. It works by starting with a single node and iteratively adding the closest node until all nodes are connected.

Kruskal's Algorithm: This algorithm is used to find the minimum spanning tree of a weighted graph. It works by sorting the edges by weight and iteratively adding the lowest weight edge that does not create a cycle.

Floyd-Warshall Algorithm: This algorithm is used to find the shortest path between all pairs of nodes in a weighted graph. It works by maintaining a matrix of the shortest distances between each pair of nodes.

These are just a few examples of the many graph algorithms that exist. The choice of algorithm depends on the specific problem that needs to be solved and the characteristics of the graph.

Graph Terminology

Adjacency: A vertex is said to be adjacent to another vertex if there is an edge connecting them. Vertices 2 and 3 are not adjacent because there is no edge between them.

Path: A sequence of edges that allows you to go from vertex A to vertex B is called a path. 0-1, 1-2 and 0-2 are paths from vertex 0 to vertex 2.

Directed Graph: A graph in which an edge (u,v) doesn't necessarily mean that there is an edge (v, u) as well. The edges in such a graph are represented by arrows to show the direction of the edge.

Vertices - are nodes of the graph
Edge - the edge is the line that connects pairs of vertices
Unweighted graph - A graph which does not have a weight associated with any edge
Weighted edge - A graph which has a weight associated with the edge
Undirected graph - In case the edges of the graph do not have a direction associated with them
Directed graph - If the edges in the graph have a directio associated with them
Cyclic graph - A graph which has atleast one loop 
Acyclic - A graph with no loop