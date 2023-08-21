# Level order traversal, also known as breadth-first traversal, is a tree traversal algorithm used to visit all the nodes in a tree or a binary tree, starting from the root node and visiting each level of the tree before moving on to the next level. It visits the nodes in the following order:

# Visit the root node.
# Visit all the nodes at level 1 (the children of the root node).
# Visit all the nodes at level 2 (the grandchildren of the root node).
# Visit all the nodes at level 3 (the great-grandchildren of the root node).
# And so on, until all the nodes in the tree have been visited.
# In other words, the level order traversal visits the nodes in order of increasing depth, from top to bottom and from left to right.

# Level order traversal is useful in a variety of binary tree problems, such as finding the minimum depth of a binary tree or finding the leftmost or rightmost node in a binary tree.

class TreeNode:
    def __init__(self, val=0, left= None, right= None):
        self.val = val
        self.left = left
        self.right = right
        
        # In this code, the TreeNode class represents a node in a binary tree, with a val attribute representing the node's value and left and right attributes representing its left and right children. The levelOrder function takes a root parameter representing the root node of the binary tree, and returns a list of integers representing the values of the nodes visited in level order.
        
def levelOrderTraversal(root: TreeNode) -> List[int]:
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        level_size = len(queue)
        level_nodes = []
        
        for i in range(level_size):
            node = queue.pop(0)
            level_nodes.append(node.val)
            
            if node.left:
                queue.append(node.left)
                
            if node.right:
                queue.append(node.right)
                
                # The function initializes an empty result list and a queue that starts with the root node. It then enters a loop that continues as long as the queue is not empty. In each iteration, the function retrieves the size of the current level by getting the length of the queue, creates an empty list level_nodes to store the values of the nodes in that level, and iterates over the nodes in the current level. For each node, it appends its value to level_nodes, and then adds its left and right children (if they exist) to the end of the queue.
        result.append(level_nodes)
        
    flat_result = [val for sublist in result for val in sublist]
    return flat_result

#     Once all the nodes in the current level have been processed, the level_nodes list is appended to the result list. This process is repeated until all the nodes in the tree have been visited.

# Finally, the function flattens the result list into a single list of values