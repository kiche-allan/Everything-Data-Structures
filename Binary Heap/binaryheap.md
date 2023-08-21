Heap data structure is a complete binary tree that satisfies the heap property, where any given node is

always greater than its child node/s and the key of the root node is the largest among all other nodes. This property is also called max heap property.
always smaller than the child node/s and the key of the root node is the smallest among all other nodes. This property is also called min heap property.

Heap Operations
Some of the important operations performed on a heap are described below along with their algorithms.

Heapify
Heapify is the process of creating a heap data structure from a binary tree. It is used to create a Min-Heap or a Max-Heap.

A binary heap is a binary tree data structure that satisfies the heap property. In a binary heap, each node has a value greater than or equal to (for max-heap) or less than or equal to (for min-heap) the values of its children. This means that the root node of a max-heap contains the largest value in the heap, while the root node of a min-heap contains the smallest value.

Binary heaps are commonly used to implement priority queues, which allow efficient insertion and deletion of elements in a dynamically changing set. The heap property guarantees that the highest priority element is always at the root of a max-heap, or the lowest priority element is always at the root of a min-heap, so it can be quickly retrieved.

Binary heaps are typically implemented as arrays, where the children of a node at index i are at indices 2i+1 and 2i+2, and the parent of a node at index i is at index floor((i-1)/2). This allows the heap to be efficiently stored in memory and provides constant-time access to the root node.

There are two types of binary heaps: max-heap and min-heap. In a max-heap, the value of each parent node is greater than or equal to the value of its children, while in a min-heap, the value of each parent node is less than or equal to the value of its children.


Heapify(array, size, i)
    set i as largest
    leftChild = 2i + 1
    rightChild = 2i + 2

    if leftChild > array[largest]
        set leftChildIndex as largest
    if rightChild > array[largest]
        set rightChildIndex as largest

    swap array[i] and array[largest]