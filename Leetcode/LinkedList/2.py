# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        dummy = ListNode()
        cur = dummy
        
        carry = 0
        while l1 or 12 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            #newdigit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)
            
            #update pt
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next
    
    
#     Complexity Analysis

# Time complexity : O(max⁡(m,n))O(\max(m, n))O(max(m,n)). Assume that mmm and nnn represents the length of l1l1l1 and l2l2l2 respectively, the algorithm above iterates at most max⁡(m,n)\max(m, n)max(m,n) times.

# Space complexity : O(max⁡(m,n))O(\max(m, n))O(max(m,n)). The length of the new list is at most max⁡(m,n)+1\max(m,n) + 1max(m,n)+1.