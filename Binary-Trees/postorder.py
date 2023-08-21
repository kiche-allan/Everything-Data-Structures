# Postorder traversal is a tree traversal algorithm used to visit all the nodes in a tree or a binary tree. It is called "postorder" because it visits the nodes in the following order:

# Traverse the left subtree in postorder.
# Traverse the right subtree in postorder.
# Visit the root node.
# In other words, the postorder traversal visits the current node after visiting both its left and right children. Here's an example of the postorder traversal of a binary tree:

# The postorder traversal of this tree would be: 4, 5, 2, 6, 3, 1. It starts by visiting the leftmost leaf node (4), then its sibling (5), then their parent (2), then the right child (6), then their parent (3), and finally the root node (1).

# Postorder traversal is useful in certain types of binary tree problems, such as calculating the height of a binary tree or evaluating the expression represented by a binary expression tree.

class TreeNode:
    def __init__(self, val = 0,left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
        
def postorderTraversal(root: TreeNode) -> List(int):
    if not root:
        return []
    
    result = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
            
    return result[::-1]

# In this code, the TreeNode class represents a node in a binary tree, with a val attribute representing the node's value and left and right attributes representing its left and right children. The postorderTraversal function takes a root parameter representing the root node of the binary tree, and returns a list of integers representing the values of the nodes visited in postorder.

# The function initializes an empty result list and a stack that starts with the root node. It then enters a loop that continues as long as the stack is not empty. In each iteration, the function pops a node from the stack, appends its value to the result list, and then pushes its right and left children (if they exist) onto the stack.

# This way, the function visits the left subtree first in postorder, then the right subtree in postorder, and finally the root node. Finally, it returns the result list with the values of all the nodes visited, but reversed since we visited the nodes in the reverse order of postorder traversal.






