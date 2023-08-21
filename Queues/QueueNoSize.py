class Queue:
    def __init__(self):
        self.items = []
        
    def __str__(self) -> str:
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    # create empty method
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
        
    #create an enqueue method
    
    def enqueue(self, value):
        self.items.append(value)
        return "The element has been successfully inserted"
    
    def dequeue(self):
        if self.isEmpty():
            return "There is no any element in the queue"
        else:
            return self.items.pop(0)
        
    #peek method
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the equeue"
        else:
            return self.items[0]
        
    #delete method
    def delete(self):
        self.items = None
        return "The queue has been successfully deleted"
        
        
    
customerQueue = Queue()
customerQueue.enqueue(1)
customerQueue.enqueue(2)
customerQueue.enqueue(3)
print(customerQueue.peek())
print(customerQueue.dequeue())
customerQueue.delete()
    
    