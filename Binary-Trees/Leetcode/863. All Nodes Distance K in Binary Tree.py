# Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

# You can return the answer in any order.

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        g = defaultdict(list)
        q = deque( [root] )
        
		# building undirected graph
        while q:
            cur = q.popleft()
            
            if cur.left:
                q.append(cur.left)
                g[cur.val].append(cur.left.val)
                g[cur.left.val].append(cur.val)
            if cur.right:
                q.append(cur.right)
                g[cur.val].append(cur.right.val)
                g[cur.right.val].append(cur.val)
        
        q = deque( [target.val] )
        seen = set( [target.val] )
        
		# BFS
        while k and q:
            k -= 1
            for _ in range(len(q)):
                cur = q.popleft()
                
                for nei in g[cur]:
                    if nei not in seen:
                        q.append(nei)
                        seen.add(nei)

        return list(q            )
    
# The code first creates an empty dictionary g using the defaultdict(list) function from the collections module. This dictionary will be used to represent an undirected graph, where each node is a key, and its adjacent nodes are stored as values in a list.
# It initializes a deque q with the root node and starts building the undirected graph using a BFS traversal. The BFS starts by popping a node from the left end of the deque and examines its left and right child, if they exist. It adds the child nodes to the deque, updates the graph g with the appropriate connections, and continues until the deque is empty.
# After building the graph, the code initializes a new deque q with the value of the target node and a set seen containing the target value. These will be used to perform BFS to find nodes at distance k from the target node.
# The code enters a loop that iterates k times (decrementing k at each iteration). In each iteration, it processes all the nodes in the current level of the BFS traversal. For each node, it retrieves its adjacent nodes from the graph and checks if they have been visited (nei not in seen). If a neighbor node hasn't been seen before, it adds it to the deque q and updates the seen set.
# Finally, the code returns the list of nodes in the deque q, which will contain the nodes at distance k from the target node.
# Note that this implementation assumes that the TreeNode class and the List and defaultdict types have been properly imported.

# Overall, the code efficiently constructs the graph using BFS and then performs BFS again to find the nodes at distance k from the target node.