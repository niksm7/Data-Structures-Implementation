class Node:
    def __init__(self,data,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class LinkedList():
    def __init__(self):
        self.head = None
    
    def insertAtBegin(self,data):
        if self.head == None:
            self.head = Node(data)
            self.head.next = self.head
            self.head.prev = self.head
        else:
            new_node = Node(data,self.head,self.head.prev)
            new_node.prev.next = new_node
            self.head.prev = new_node
            self.head = new_node

    def insertAtEnd(self,data):
        if self.head == None:
            self.head = Node(data)
            self.head.next = self.head
            self.head.prev = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = Node(data,self.head,temp)
            self.head.prev = temp.next
    
    def deleteFirst(self):
        if self.head == None:
            print("List is empty")
        
        else:
            self.head.prev.next = self.head.next
            self.head.next.prev = self.head.prev
            self.head = self.head.next



    def deleteLast(self):
        if self.head == None:
            print("List is empty")
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.prev.next = self.head
            self.head.prev = temp.prev
        

    def printList(self):
        if self.head == None:
            print("List is Empty")
        else:
            print(f"tail({self.head.prev.data})","<->",end=" ")
            print(self.head.data,"<->",end=" ")
            temp = self.head.next
            while temp != self.head:
                print(temp.data,"<->",end=" ")
                temp = temp.next
            print(f"head({temp.data})",end="\n")


if __name__ == "__main__":
    l = LinkedList()
    l.insertAtEnd(2)
    l.insertAtEnd(4)
    l.insertAtEnd(5)
    l.insertAtBegin(1)

    l.printList()

    l.deleteFirst()

    l.printList()

    l.deleteLast()

    l.printList()
    