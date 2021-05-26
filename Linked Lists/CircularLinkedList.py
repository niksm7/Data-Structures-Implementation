class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtEnd(self,data):
        if self.head == None:
            self.head = Node(data)
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = Node(data,self.head)

    def inserAtBeginning(self,data):
        if self.head == None:
            self.head = Node(data)
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = Node(data,self.head)
            self.head = temp.next
    

    def deleteFirstNode(self):
        if self.head == None:
            print("List is Empty! Can't delete")
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head.next
            self.head = temp.next

    def deleteLastNode(self):
        if self.head == None:
            print("List is Empty! Can't delete")
        else:
            temp = self.head
            prev_temp = 0
            while temp.next != self.head:
                prev_temp = temp
                temp = temp.next
            prev_temp.next = self.head

    def printList(self):
        if self.head == None:
            print("List is Empty")
        else:
            print(self.head.data)
            i = self.head
            while i.next != self.head:
                i = i.next
                print(i.data)

if __name__ == "__main__":
    l = LinkedList()
    l.insertAtEnd(2)
    l.insertAtEnd(4)
    l.insertAtEnd(5)
    l.insertAtEnd(6)
    l.inserAtBeginning(1)
    l.deleteLastNode()
    l.deleteFirstNode()
    l.inserAtBeginning(8)
    l.printList()
