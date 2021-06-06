class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        if self.head == None:
            return True
        return False

    def EnQueue(self,data):

        newnode = Node(data)

        if self.isEmpty():
            self.head = self.tail = newnode

        else:
            self.tail.next = newnode
            self.tail = self.tail.next

    def DeQueue(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            self.head = self.head.next
    
    
    def printList(self):
        
        temp = self.head
        while temp != None:
            print(temp.data,end=" ")
            temp = temp.next
        print("\n")


if __name__ == "__main__":
    qu = LinkedList()
    qu.EnQueue(1)
    qu.EnQueue(5)
    qu.EnQueue(9)
    qu.EnQueue(12)
    qu.printList()
    qu.DeQueue()
    qu.DeQueue()
    qu.printList()