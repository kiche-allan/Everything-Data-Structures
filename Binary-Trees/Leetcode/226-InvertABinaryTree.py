class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        
        #postorder traversal
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        #swap the children, right and left subtree
        root.left, root.right = root.right, root.left
        
        return root
    
#SOLUTION 2

         
# Intuition
# My first thought upon reading the problem statement is that this is a simple tree traversal and modification problem. Inverting a binary tree means swapping the left and right subtrees of each node in the tree, so I would need to traverse the tree and swap the subtrees recursively.

# I would likely use a depth-first search (DFS) approach to traverse the tree, and for each node, swap its left and right subtrees using a temporary variable. I would continue this process for each node in the tree until I have swapped all the subtrees. Finally, I would return the root node of the inverted tree.

# Overall, my approach would be to carefully read and understand the problem statement, and then brainstorm possible solutions based on my existing knowledge of binary trees, DFS traversal, and recursive programming techniques.

# Approach
# To solve the problem of inverting a binary tree, my approach would be to traverse the tree in a post-order traversal (left subtree, right subtree, root) and swap the left and right subtrees at each node. This can be done recursively, as follows:

# Base case: If the root is None, return None.
# Recursively invert the left and right subtrees of the root.
# Swap the left and right subtrees of the root.
# Return the inverted root.
# This approach works because we are essentially flipping the tree upside down, starting from the leaves and working our way up to the root. At each node, we swap its left and right subtrees to invert the entire subtree rooted at that node.

# To implement this approach in code, I would define a recursive function called "invertTree" that takes in the root of the tree and returns the inverted root. Inside the function, I would first check if the root is None, and if so, return None. Otherwise, I would recursively invert the left and right subtrees of the root by calling "invertTree" on each subtree. Then, I would swap the left and right subtrees of the root by assigning the left subtree to a temporary variable, setting the left subtree to the inverted right subtree, and setting the right subtree to the inverted temporary left subtree. Finally, I would return the inverted root.

# Complexity
# Time complexity:
# The time complexity of the above solution is O(n), where n is the total number of nodes in the binary tree. This is because the algorithm visits each node once and performs constant-time operations for each node.

# Space complexity:
# The space complexity of the above solution is also O(n), where n is the total number of nodes in the binary tree. This is because the space used by the call stack of the recursive function is proportional to the height of the tree, and in the worst case, the tree can be skewed, resulting in a height of n. Therefore, the space complexity is linear with respect to the number of nodes in the binary tree.