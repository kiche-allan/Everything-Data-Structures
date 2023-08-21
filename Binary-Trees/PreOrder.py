# Preorder traversal is a type of tree traversal algorithm used to visit all the nodes in a tree or a binary tree. It is called "preorder" because it visits the nodes in the following order:

# Visit the root node.
# Traverse the left subtree in preorder.
# Traverse the right subtree in preorder.
# In other words, the preorder traversal visits the current node before visiting its children. Here's an example of the preorder traversal of a binary tree:

# Preorder traversal is useful in certain types of binary tree problems, such as building an expression tree or converting a tree to a linked list.

class TreeNode:
    def __init__(self, val =0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
def preorderTraversal(root: TreeNode):
    if not root:
        return []
        # print(root.val)
        # preorderTraversal(root.left)
        # preorderTraversal(root.right)
    result = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
            
    return result
    
    
# In this code, the TreeNode class represents a node in a binary tree, with a val attribute representing the node's value and left and right attributes representing its left and right children. The preorderTraversal function takes a root parameter representing the root node of the binary tree, and returns a list of integers representing the values of the nodes visited in preorder.

# The function initializes an empty result list and a stack that starts with the root node. It then enters a loop that continues as long as the stack is not empty. In each iteration, the function pops a node from the stack, appends its value to the result list, and then pushes its right and left children (if they exist) onto the stack.

# This way, the function visits the root node first, then the left subtree in preorder, and then the right subtree in preorder. Finally, it returns the result list with the values of all the nodes visited.