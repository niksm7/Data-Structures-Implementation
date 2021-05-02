# This Queue is similar to the normal Queue except that- 

# We need to delete the number with maximum priority first (here max priority is the maximum number)

# If there are two numbers with equal priority then we take the one which comes first from left i.e FIFO

class PriorityQueue():

    def __init__(self):
        self.queue = []
    
    def insert(self,data):
        self.queue.append(data)
    
    def delete(self):
        if not self.isEmpty():

            max_ele = max(self.queue)
            indexof_max_ele = self.queue.index(max_ele)

            return self.queue.pop(indexof_max_ele)

        return -1

    def isEmpty(self):
        return self.queue == []
    
    def printQueue(self):
        print(*self.queue)

if __name__ == "__main__":
    PQ = PriorityQueue()

    PQ.insert(18)
    PQ.insert(7)
    PQ.insert(21)
    PQ.insert(4)
    PQ.insert(21)
    print("Current Queue - ",end="")
    PQ.printQueue()

    PQ.delete()
    print("After 1 Deletion - ",end="")
    PQ.printQueue()
    
    PQ.delete()
    print("After 2 Deletion - ",end="")
    PQ.printQueue()

