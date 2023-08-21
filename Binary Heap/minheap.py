class MinHeap:
    def __init__(self):
        self.heap = []
        
    def parent(self, i):
        return (i-1)//2
    
    def left_child(self, i):
        return 2*i + 1
    
    def right_child(self, i):
        return 2*i + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        
    def insert(self, item):
        self.heap.append(item)
        i = len(self.heap) - 1
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.swap(i, self.parent(i))
            i = self.parent(i)
            
    def min_heapify(self, i):
        l = self.left_child(i)
        r = self.right_child(i)
        smallest = i
        if l < len(self.heap) and self.heap[l] < self.heap[i]:
            smallest = l
        if r < len(self.heap) and self.heap[r] < self.heap[smallest]:
            smallest = r
        if smallest != i:
            self.swap(i, smallest)
            self.min_heapify(smallest)
            
    def extract_min(self):
        if len(self.heap) == 0:
            return None
        min_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.min_heapify(0)
        return min_val
# Example usage
min_heap = MinHeap()
min_heap.insert(5)
min_heap.insert(3)
min_heap.insert(8)
min_heap.insert(2)
min_heap.insert(7)
min_heap.print_heapify() # Output: [8, 7, 5, 2, 3]
