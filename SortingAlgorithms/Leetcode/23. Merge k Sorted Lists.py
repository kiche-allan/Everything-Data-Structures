# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.
import heapq
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        
class Solutions:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        #initialize the heap
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next
                
        #create a dummy node
        dummy = ListNode()
        curr = dummy
        
        while heap:
            #pop the minimum node from the heapq
            val, idx = heapq.heappop(heap)
            #append the node to the sorted linked list
            curr.next = ListNode(val)
            curr = curr.next
            
            #check if there is a next node i the ame list
            if lists[idx]:
                heapq.heappush(heap, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return dummy.next
            