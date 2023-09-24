class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            res = 1 if node.val >= max_val else 0
            # then update maxvalue
            max_val = max(max_val , node.val)

            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res 