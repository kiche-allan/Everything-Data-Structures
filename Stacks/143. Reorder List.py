# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #step 1: find the middle
        if not head:
            return []
        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        #step 2 revverse the second half
        prev, curr = None, slow.next
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        slow.next = None

        #step 3 : merge lists
        head1, head2 = head, prev
        while head2:
            next = head1.next
            head1.next = head2
            head1 = head2
            head2 = next

        

