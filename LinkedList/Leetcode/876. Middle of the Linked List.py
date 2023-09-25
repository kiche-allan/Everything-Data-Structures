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