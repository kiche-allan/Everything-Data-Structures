# Inorder traversal is another type of tree traversal algorithm used to visit all the nodes in a tree or a binary tree. It is called "inorder" because it visits the nodes in the following order:

# Traverse the left subtree in inorder.
# Visit the root node.
# Traverse the right subtree in inorder.
# In other words, the inorder traversal visits the current node after visiting its left child but before visiting its right child. Here's an example of the inorder traversal of a binary tree:

# Inorder traversal is useful in certain types of binary tree problems, such as finding the k-th smallest element in a binary search tree or checking if a binary tree is a valid binary search tree.

# Implementation
from ast import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def inorderTraversal(root: TreeNode) -> List[int]:
    if not root:
        return []
    
    result = []
    stack = []
    
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
            
        root = stack.pop()
        result.append(root.val)
        root = root.right
        
    return result

# In this code, the TreeNode class represents a node in a binary tree, with a val attribute representing the node's value and left and right attributes representing its left and right children. The inorderTraversal function takes a root parameter representing the root node of the binary tree, and returns a list of integers representing the values of the nodes visited in inorder.

# The function initializes an empty result list and a stack. It then enters a loop that continues as long as the stack is not empty or there are nodes left to visit. In each iteration, the function pushes all the left children of the current node onto the stack, then pops a node from the stack, appends its value to the result list, and then sets the current node to its right child (if it exists).

# This way, the function visits the leftmost node first, then its parent, then its right child (if it exists), then its parent's parent, and so on, until it has visited all the nodes in the tree in inorder. Finally, it returns the result list with the values of all the nodes visited.