class Queue():

    def __init__(self,limit=10):
        self.queue = []
        self.limit = limit
        self.length = 0
    
    def enqueue(self,data):
        if self.length >= self.limit:
            print("Queue Overflow")
        else:
            self.queue.append(data)
            self.length += 1
    
    def dequeue(self):
        if self.length == 0:
            return "Empty Queue"
        else:
            x = self.queue[0]
            self.queue = self.queue[1:]
            self.length -= 1
            return x

    def isEmpty(self):
        return self.length == 0
    
    def getSize(self):
        return self.length

    def printQueue(self):
        print([i for i in self.queue])



if __name__ == "__main__":
    n = 12 # Fixed size of our Queue

    myQueue = Queue(n)
    
    print("Is Queue Empty? -",myQueue.isEmpty())

    for i in range(n):
        myQueue.enqueue(i+1)

    print("Size of Queue",myQueue.getSize())

    print("Is Queue Empty?-",myQueue.isEmpty())
    
    print("Dequed Element - ",myQueue.dequeue())

    print("Size of Queue - ",myQueue.getSize())

    myQueue.printQueue()

