# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        current = head
        while current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head

#approach
# The approach to deleting duplicates from a sorted linked list involves iterating through the list and adjusting the pointers to skip duplicate nodes. Here's a step-by-step explanation:

# Initialize Pointers:

# Create a pointer current and set it to the head of the linked list.
# Iterate through the List:

# Use a while loop to traverse the linked list.
# Check for Duplicates:

# Inside the loop, check if the current node has the same value as the next node (current.val == current.next.val).
# Skip Duplicates:

# If duplicates are found, update the next pointer of the current node to skip the duplicate node (current.next = current.next.next).
# Move to the Next Node:

# If no duplicates are found, move the current pointer to the next node in the list (current = current.next).
# Repeat:

# Continue this process until the end of the linked list is reached (while current and current.next).
# Return Modified Linked List:

# Finally, return the modified linked list (head).
# The key idea is to use the current pointer to iterate through the list, and when a duplicate is found, adjust the pointers to skip that duplicate node. This way, the modified linked list will only contain unique elements, and the order of elements will be preserved since the list is initially sorted. The time complexity of this solution is O(n), where n is the number of nodes in the linked list, as we traverse the list once.