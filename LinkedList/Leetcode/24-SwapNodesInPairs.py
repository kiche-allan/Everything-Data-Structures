# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        previous, current = dummy, head
         
        while current and current.next:
            #save the pairs
            nextPair = current.next.next
            second = current.next

            #reverse the pair of nodes
            second.next = current
            current.next = nextPair
            previous.next = second
             
            #update our pairs
            previous = current
            current = nextPair
             
        return dummy.next
    
#     This is a correct solution to the problem of swapping every two adjacent nodes in a linked list.

# The dummy node serves as a placeholder for the head of the list. previous and current are pointers that allow us to traverse the list. We iterate through the list until there are no more pairs to swap. For each pair, we save a reference to the node after the pair (nextPair), and then swap the pair of nodes by updating their next pointers. Finally, we update our previous and current pointers to move to the next pair.

# This solution has a time complexity of O(n), where n is the length of the list, since we need to traverse the entire list once. It also has a space complexity of O(1), since we are only creating a constant number of extra variables (i.e., dummy, previous, current, and nextPair) and not storing any additional data structures.

# Intuition
# To swap every two adjacent nodes in a linked list without modifying the values, I would use pointers to traverse the list and swap pairs of nodes. Specifically, I would create a dummy node as the head of the list and initialize two pointers to it: previous and current. Then, I would iterate through the list using these pointers, swapping pairs of adjacent nodes until there are no more pairs left to swap. For each pair, I would need to save a reference to the node after the pair, swap the pair of nodes by updating their next pointers, and update the previous and current pointers to move to the next pair. Finally, I would return the head of the list, which is the node after the dummy node.

# Approach
# My approach to solving the problem of swapping every two adjacent nodes in a linked list without modifying the values would be to use pointers to traverse the list and swap pairs of nodes. Specifically, I would create a dummy node as the head of the list and initialize two pointers to it: previous and current. Then, I would iterate through the list using these pointers, swapping pairs of adjacent nodes until there are no more pairs left to swap.

# For each pair, I would need to save a reference to the node after the pair, swap the pair of nodes by updating their next pointers, and update the previous and current pointers to move to the next pair. Finally, I would return the head of the list, which is the node after the dummy node.

# Complexity
# Time complexity:
# The time complexity of the above solution is O(n), where n is the number of nodes in the linked list. This is because we are iterating through each node in the list once, and each swap operation takes constant time.

# Space complexity:
# The space complexity of the solution is O(1), since we are only using a constant amount of extra space to store the previous, current, and nextPair pointers, regardless of the size of the linked list. This means that the space required by the algorithm does not grow with the input size, and is therefore constant or "bounded".