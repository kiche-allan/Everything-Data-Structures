class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []  # initialize an empty list to store the level order traversal of the tree

        q = collections.deque()  # initialize a deque to store the nodes to be processed
        q.append(root)  # add the root of the tree to the deque

        while q:  # while the deque is not empty
            qLen = len(q)  # get the length of the deque
            level = []  # initialize an empty list to store the nodes at the current level
            for i in range(qLen):  # iterate over the nodes at the current level
                node = q.popleft()  # remove the first node from the deque
                if node:  # if the node exists
                    level.append(node.val)  # add its value to the level list
                    q.append(node.left)  # add its left child to the deque
                    q.append(node.right)  # add its right child to the deque
            if level:  # if the level list is not empty
                res.append(level)  # add the level list to the result list
        return res  # return the result list containing the level order traversal

# The code first initializes an empty list res to store the level order traversal of the tree. Then it initializes a deque q to store the nodes to be processed, and adds the root of the tree to the deque.

# Next, the code enters a while loop that continues as long as there are nodes in the deque. Inside the loop, it gets the length of the deque and initializes an empty list level to store the nodes at the current level. Then, it iterates over the nodes at the current level using a for loop.

# Inside the for loop, the code removes the first node from the deque using popleft(). If the node exists (i.e., is not None), it adds its value to the level list and its left and right children to the deque using append().

# After processing all the nodes at the current level, the code checks if the level list is not empty. If it is not empty, it adds the level list to the res list. This process repeats until there are no more nodes in the deque.

# Finally, the code returns the res list containing the level order traversal of the tree.




# This is a solution to the problem of performing a level order traversal of a binary tree using breadth-first search (BFS) algorithm. Here is a brief explanation of the code:

# We initialize an empty list res to store the result of the level order traversal.
# We use a deque data structure to store the nodes of the binary tree. We append the root of the tree to the deque.
# While the deque is not empty, we get the number of nodes at the current level by using the len() function to get the length of the deque. We initialize an empty list level to store the values of the nodes at the current level.
# We loop through the nodes at the current level by iterating i from 0 to qLen - 1.
# For each node in the current level, we remove it from the left end of the deque using the popleft() function.
# If the node exists, we append its value to the level list and append its left and right children to the deque.
# After we have processed all the nodes at the current level, we append the level list to the res list if it is not empty.
# We return the res list as the result of the level order traversal.
# This algorithm has a time complexity of O(N), where N is the number of nodes in the binary tree. This is because we need to visit each node exactly once. The space complexity of this algorithm is also O(N), as we need to store at most N nodes in the deque.
 