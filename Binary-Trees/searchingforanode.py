# To search for a node in a binary tree, you can use a depth-first search algorithm, such as a recursive approach. Here's how you can implement it in Python:

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
        # In this code, the TreeNode class represents a node in a binary tree, with a val attribute representing the node's value and left and right attributes representing its left and right children
        
def searchBST(root: TreeNode, val: int) -> TreeNode:
    if not root or root.val == val:
        return root
    
    # The searchBST function takes two parameters: a root parameter representing the root node of the binary tree, and a val parameter representing the value to search for in the tree. The function returns the node with the given value if it is found in the tree, or None if it is not.
    
    
    if val < root.val:
        return searchBST(root.left, val)
    else:
        return searchBST(root.right, val)
    
#     The searchBST function first checks if the root node is None or has the value we are looking for. If so, it returns the root node. If not, it checks whether the value we are searching for is less than the root value. If it is, it recursively calls searchBST with the left child of the root node. If not, it recursively calls searchBST with the right child of the root node.

# This algorithm has a time complexity of O(h), where h is the height of the binary tree. In the worst case, when the tree is skewed, the time complexity is O(n), where n is the number of nodes in the tree.




