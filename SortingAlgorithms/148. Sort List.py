# Given the head of a linked list, return the list after sorting it in ascending order.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        temp = []

        while cur:
            temp.append(cur.val)
            cur = cur.next

        temp.sort()
        dummy = ListNode(0)
        cur = dummy

        for v in temp:
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next
             

