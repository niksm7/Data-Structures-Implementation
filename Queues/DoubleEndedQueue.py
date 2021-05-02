# A type of Queue where we can add from both ends and remove from both ends

class Deque:

    def __init__(self):
        self.items = []

    def addRear(self,data):
        self.items.insert(0,data)
    
    def addFront(self,data):
        self.items.append(data)
    
    def removeRear(self):
        if not self.isEmpty():
            return self.items.pop(0)
        return "Queue Empty"
    
    def removeFront(self):
        if not self.isEmpty():
            return self.items.pop(-1)
        return "Queue Empty"
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)



if __name__ == "__main__":

    d=Deque()
    print("Is Queue Empty? - ",d.isEmpty())

    d.addRear(4)

    d.addRear('dog')

    d.addFront('cat')

    d.addFront(23)

    print("Current Items - ", d.items)
    print("Current Size of Queue - ",d.size())
    print("Is Queue Empty? - ", d.isEmpty())

    d.addRear(8.4)

    print("Element removed from Rear end - ",d.removeRear())
    print("Element removed from Front end - ", d.removeFront())
    print("Current Items - ",d.items)
    
    d.removeRear()
    d.removeRear()
    d.removeRear()
    print(d.removeRear())