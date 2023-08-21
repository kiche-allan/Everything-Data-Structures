# 297. Serialize and Deserialize Binary Tree


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)
        

    def deserialize(self, data):
       
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

# Intuition
# When presented with the problem of serializing and deserializing a binary tree, my initial thoughts would be to consider the structure of the binary tree and how it could be represented as a string. One possible approach would be to traverse the tree in a depth-first manner and represent each node as a string containing its value and whether it has left and right child nodes. Then, the entire tree can be represented as a string by concatenating the strings for each node in the appropriate order. To deserialize the tree, we could simply split the string representation and recursively construct the tree by creating new nodes for each value in the correct order.

# Another possible approach would be to consider the binary tree as a graph and use graph traversal algorithms to serialize and deserialize it. For example, we could use a breadth-first search to traverse the tree and store each node's value and child nodes in a list, which can be converted to a string. To deserialize the tree, we could simply convert the string back into a list and use a breadth-first search to construct the tree by creating new nodes for each value in the correct order.

# Overall, the key to solving this problem is to come up with a clear and systematic approach to representing the binary tree as a string and constructing the tree from the string.

# Approach
# The problem of serializing and deserializing a binary tree can be solved using a recursive depth-first approach. The idea is to traverse the binary tree in a depth-first manner and store each node's value and child nodes in a string representation. To deserialize the tree, we simply convert the string representation back into a binary tree.

# The serialization algorithm can be implemented using a recursive depth-first traversal of the binary tree. At each node, we append its value to the serialized string, followed by a delimiter character. We then recursively call the serialization function on the node's left child, and then on the node's right child. If the node has no children, we append a special character to the serialized string to indicate the absence of a child.

# The deserialization algorithm can be implemented using a recursive approach as well. We split the serialized string into a list of values using the delimiter character. We then recursively create new nodes for each value in the correct order, starting with the root node. If the value indicates the absence of a child, we set the child node to None. Otherwise, we create a new node with the value and set its left and right child nodes by recursively calling the deserialization function.

# Overall, this approach is simple, efficient, and can handle any binary tree structure.

# Complexity
# Time complexity:
# The time complexity of the serialization and deserialization algorithms for a binary tree is O(n), where n is the number of nodes in the binary tree. This is because both algorithms visit each node exactly once, so the time complexity is proportional to the number of nodes in the tree.

# Space complexity:
# The space complexity of the serialization algorithm is also O(n), where n is the number of nodes in the binary tree. This is because the algorithm stores the serialized string in memory, which requires O(n) space to store all the node values.
    
# In the serialize function, a list res is used to store the serialized values of the tree nodes. The dfs function is a helper function that recursively visits each node in a depth-first manner and adds its value to the res list. If the node is None, the string "N" is added to represent the absence of a node.

# In the deserialize function, the serialized string data is split into a list of values vals. The dfs function is a helper function that recursively constructs the tree by visiting each node in the same order as the serialize function. If the current value vals[i] is "N", it means that there is no child node at that position, so it returns None. Otherwise, it creates a new TreeNode with the value vals[i], sets its left and right child nodes using recursive calls to dfs, and returns the new node.

# Overall, this implementation correctly serializes and deserializes binary trees, and the serialize function returns a string while the deserialize function returns a tree.

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))