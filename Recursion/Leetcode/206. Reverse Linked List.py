# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

class Solution:
    def reverseList(self, head:Optional[ListNode]) -> Optional[ListNode]:
        prev = None #initialize a previous node as None
        curr = head # initialize the current node as a head
        
        while curr:
            temp = curr.next #store the next node in a temporary variable. This is needed because we are going to change the next of the current node
            curr.next = prev #update the next of the current node to point to the previous node
            prev = curr #move the previous node pointer to the current node
            curr = temp
            
        return prev #prev will be the new head of the reversed list
    
#     Intuition
# Initialize three pointers - prev, curr, and next - to keep track of the previous node, current node, and the next node, respectively.
# Traverse the linked list in pairs, updating the next pointers to swap adjacent nodes.
# Update the prev and curr pointers accordingly for the next iteration.
# Continue this process until we reach the end of the list or there is only one node left.
# Return the head of the modified linked list, which would be the second node after swapping.

# Approach
# Initialize three pointers - prev, curr, and next - to None, head, and None, respectively, to keep track of the previous node, current node, and the next node.
# While curr is not None:
# Set next to curr.next, which is the next node in the original list.
# Update curr's next pointer to prev, effectively reversing the link of the current node to point to the previous node.
# Update prev to curr, and curr to next for the next iteration.
# After the loop, return prev as the new head of the reversed linked list.

# Complexity
# Time complexity:
# The time complexity of the solution is O(n), where n is the number of nodes in the linked list. This is because we need to visit each node in the list exactly once, and the number of operations performed for each node is constant. Specifically, we perform constant-time operations such as pointer assignments, comparisons, and updates for each node in the list.

# Space complexity:
# Space Complexity:
# The space complexity of the solution is O(1), as we are using a constant amount of extra space to keep track of the three pointers (prev, curr, next). We are not using any additional data structures or allocating any new memory, and the amount of extra space used remains constant regardless of the size of the input linked list.