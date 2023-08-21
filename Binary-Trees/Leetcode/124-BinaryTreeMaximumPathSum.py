
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def maxPathSumHelper(node):
            if node is None:
                return 0

            left_sum = max(0, maxPathSumHelper(node.left))
            right_sum = max(0, maxPathSumHelper(node.right))

            current_sum = node.val + left_sum + right_sum

            self.max_sum = max(self.max_sum, current_sum)

            return node.val + max(left_sum, right_sum)

        maxPathSumHelper(root)
        return self.max_sum

# Intuition
# One approach to solve this problem is to use depth-first search (DFS) to traverse the binary tree and keep track of the maximum path sum encountered so far. In order to compute the maximum path sum at each node, we need to consider both the path that includes the node and the path that goes through one of the node's subtrees. We can use a recursive function to perform the DFS traversal and compute the maximum path sum for each node. At each node, we can update the maximum path sum encountered so far, which will be the solution to the problem.

# Approach
# To solve this problem, I will use a recursive approach. I will define a function called dfs that takes a node as input and returns the maximum path sum that includes this node. This function will compute the maximum path sum with and without the node's children. To compute the maximum path sum with the node's children, I will recursively call dfs on the left and right child of the node. I will then add the node's value to the maximum of the maximum path sum of the left and right child. To compute the maximum path sum without the node's children, I will recursively call dfs on the left and right child of the node, and I will return the maximum of the maximum path sum of the left and right child. Finally, I will compute the maximum path sum with and without the root node and return the maximum of the two.

# Complexity
# Time complexity:
# The time complexity of the maxPathSum function is O(N), where N is the number of nodes in the binary tree. This is because we visit each node exactly once during the depth-first search traversal of the tree.

# Space complexity:
# The space complexity of the maxPathSum function is O(H), where H is the height of the binary tree. This is because the maximum depth of the recursion is equal to the height of the tree. In the worst case, the binary tree can be skewed, and the height of the tree can be equal to the number of nodes in the tree, making the space complexity O(N).

# Code
# class Solution:
#     def maxPathSum(self, root: TreeNode) -> int:
#         res = [root.val]
        
#         #return max path sum without split
        
#         def dfs(root):
#             if not root:
#                 return 0
            
#             leftMax = dfs(root.left)
#             rightMax = dfs(root.right)
#             leftMax = max(leftMax, 0)
#             rightMax = max(rightMax, 0)
            
#             #compute max path sum with split
#             res[0] = max(res[0], root.val + leftMax + rightMax)
            
#             return root.val + max(leftMax, rightMax)