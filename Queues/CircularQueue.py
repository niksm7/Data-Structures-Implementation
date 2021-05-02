class CircularQueue():

    def __init__(self,limit):
        self.queue = []
        self.limit = limit
        self.rear = self.front = None
        self.size = 0
    

    def enqueue(self,data):
        
        if self.isFull():
            print("Queue is Full")
        
        else:
            self.queue.append(data)
        
        if self.front is None:
            self.front = self.rear = 0
        else:
            self.rear = self.size

        self.size += 1

    def dequeue(self):

        if self.isEmpty():
            return "Queue is Empty"
        
        else:
            ele = self.queue.pop(0)
            self.size -= 1
            if self.size == 0:
                self.front = self.rear = 0
            
            else:
                self.rear = self.size - 1

            return ele


    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size >= self.limit
    
    def sizeOf(self):
        return self.size

    def printQueue(self):
        print(*self.queue)

if __name__ == "__main__":

    cq = CircularQueue(5)

    cq.enqueue(4)
    cq.enqueue(12)
    cq.enqueue(10)
    cq.enqueue(9)
    cq.enqueue(14)
    cq.enqueue(21)
    cq.printQueue()
    print(cq.sizeOf())

    cq.dequeue()
    cq.printQueue()
    print(cq.sizeOf())
    