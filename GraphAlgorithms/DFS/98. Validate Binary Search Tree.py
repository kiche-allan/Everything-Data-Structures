# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left 
# subtree
#  of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False
            if not (node.val < right and node.val > left):
                return False
            return (valid(node.left, left, node.val) and 
                    valid(node.right, node.val, right))
        return valid(root, float('-inf'), float('inf'))
            
# class Solution:: This code seems to be a part of a class definition. It defines a class named "Solution" that potentially contains other methods related to solving a particular problem.

# def isValidBST(self, root: TreeNode) -> bool:: This is a method definition named "isValidBST" within the "Solution" class. It takes two parameters: self, which represents the instance of the class, and root, which is expected to be an instance of the TreeNode class. The return type of this method is specified as bool, indicating that it returns a boolean value.

# def valid(node, left, right):: This is a nested helper function named "valid". It takes three parameters: node represents the current node being checked, left represents the lower bound of the valid range for values in the left subtree, and right represents the upper bound of the valid range for values in the right subtree.

# if not node:: This condition checks if the node parameter is None (or null). If node is None, it means we have reached the end of a branch, and it returns True to indicate that the subtree is a valid BST.

# if not (node.val < right and node.val > left):: This condition checks if the value of the current node violates the ordering property of the BST. It compares the value of node.val with the valid range represented by left and right. If the value is not within this range, it returns False to indicate that the subtree is not a valid BST.

# return (valid(node.left, left, node.val) and valid(node.right, node.val, right)): This recursive line invokes the valid function on the left and right subtrees of the current node. It checks if both subtrees are valid BSTs based on the updated range. It returns True only if both the left and right subtrees are valid BSTs.

# return valid(root, float('-inf'), float('inf')): This line initiates the recursion by calling the valid function with the root node of the entire tree and initial range values of negative infinity and positive infinity. It returns the result of the valid function, which determines whether the entire tree is a valid BST.

# In summary, the code checks the validity of a binary search tree by recursively traversing the tree and comparing each node's value with the appropriate range of valid values. It returns True if the tree is a valid BST and False otherwise.