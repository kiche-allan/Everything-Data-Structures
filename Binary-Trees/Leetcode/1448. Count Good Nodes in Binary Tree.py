# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

# Return the number of good nodes in the binary tree.

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_val):
            if not node:
                return 0
            res = 0
            if node.val >= max_val:
                res += 1
                max_val = node.val

            res += dfs(node.left, max_val)
            res += dfs(node.right, max_val)
            return res

        if not root:
            return 0
        return dfs(root, root.val)
    
# class Solution:: Defines a class named Solution.

# def goodNodes(self, root: TreeNode) -> int:: Defines a method named goodNodes within the Solution class. This method takes two parameters: self (a reference to the instance of the class) and root (a parameter of type TreeNode representing the root of a binary tree). The method is expected to return an integer.

# def dfs(node, max_val):: Defines a nested function named dfs (depth-first search). This function takes two parameters: node (representing the current node in the traversal) and max_val (the maximum value encountered in the path from tghe root to the current node).

# if not node:: Checks if the current node is None, indicating the end of a branch. In this case, the function returns 0.

# good_count = 0: Initializes a variable good_count to keep track of the count of "good" nodes encountered in the subtree.

# if node.val >= max_val:: Checks if the value of the current node is greater than or equal to the max_val encountered so far. If it is, the current node is considered "good," and the good_count is incremented by 1. The max_val is also updated to the value of the current node.

# good_count += dfs(node.left, max_val): Recursively calls the dfs function on the left child of the current node, passing along the current max_val. The count of "good" nodes returned from this recursive call is added to good_count.

# good_count += dfs(node.right, max_val): Recursively calls the dfs function on the right child of the current node, passing along the current max_val. The count of "good" nodes returned from this recursive call is added to good_count.

# return good_count: Returns the total count of "good" nodes encountered in the subtree rooted at the current node.

# if not root:: Checks if the root node is None, indicating an empty tree. In this case, the method returns 0.

# return dfs(root, root.val): Calls the dfs function on the root node, passing the root node itself as well as its value (root.val) as the initial max_val. The result of this function call is returned as the final count of "good" nodes.

# Overall, the code defines a class Solution with a method goodNodes that implements a depth-first traversal of a binary tree while keeping track of the maximum value encountered. It counts and returns the number of "good" nodes in the binary tree.