# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.



class Solution:
    def middleLinkedList(self, head: ListNode) -> ListNode:
        #initialize the two pointers 
        slow_pointer = head
        fast_pointer = head

        # use the while loop

        while fast_pointer and fast.pointer.next:
            slow_pointer = slow_pointer.next

            fast_pointer = fast_pointer.next.next

        return slow_pointer

# Here's a detailed explanation of how to find the middle node of a singly linked list, prioritizing the second middle node in cases with even numbers of nodes:

# 1. Two-Pointer Approach (Optimal):

# Initialize two pointers:
# slow: Points to the head of the list.
# fast: Points to the head of the list as well.
# Iterate through the list:
# Move fast two nodes ahead for each move of slow.
# When fast reaches the end (or one node before the end for even-length lists), slow will be pointing to the middle node.
# Return slow:
# It now holds the second middle node in cases with even numbers of nodes.
# Time Complexity: O(n)
# Space Complexity: O(1)

# Python Implementation: