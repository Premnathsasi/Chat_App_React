class Queue:
    def __init__(self):
        self.queue=[]

    def is_empty(self):
        return len(self.queue)==0

    def enqueue(self,val):
        self.queue.append(val)

    

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)
    
    def display(self):
        return self.queue

    def size(self):
        return len(self.queue)
    
    def front(self):
        return self.queue[0]
    
    def rear(self):
        return self.queue[-1]
    
newQueue = Queue()
newQueue.enqueue(5)
newQueue.enqueue(10)
newQueue.enqueue(15)
newQueue.enqueue(20)
print(newQueue.is_empty())
print(newQueue.display())
print(newQueue.dequeue())
print(newQueue.size())
print(newQueue.front())
print(newQueue.dequeue())
print(newQueue.rear())
print(newQueue.display())


    