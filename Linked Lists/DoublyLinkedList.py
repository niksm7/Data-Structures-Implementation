class Node:
    def __init__(self,data,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class LinkedList():
    def __init__(self):
        self.head = None
    
    def insertAtBegin(self,data):
        new_node = Node(data,self.head)
        if self.head != None:
            self.head.prev = new_node
        self.head = new_node
    
    def insertAfterGiven(self,after,data):
        if self.head == None:
            print("List Empty!")
        else:
            temp = self.head
            while temp.next != None:
                if temp.data == after:
                    new_node = Node(data,temp.next,temp)
                    temp.next = new_node
                    new_node.next.prev = new_node
                    return
                temp = temp.next
            print("Element Not Found!")
    
    def insertBeforeGiven(self,before,data):
        if self.head == None:
            print("List Empty!")
        else:
            temp = self.head
            while temp.next != None:
                if temp.data == before:
                    new_node = Node(data,temp,temp.prev)
                    temp.prev = new_node
                    new_node.prev.next = new_node
                    return
                temp = temp.next
            print("Element Not Found!")

    def insertAtEnd(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = Node(data,None,temp)
    
    def deleteFirst(self):
        if self.head == None:
            print("List is empty")
        
        else:
            self.head = self.head.next
            self.head.prev = None

    def deleteBeforeGiven(self,before):
        if self.head == None:
            print("List is Empty!")
        else:
            temp = self.head
            while temp != None:
                if temp.data == before:
                    if temp == self.head:
                        print("Given data is the first element!")
                    else:
                        temp.prev = temp.prev.prev
                        temp.prev.next = temp
                    return
                temp = temp.next
            print("Element Not Found!")
    
    def deleteAfterGiven(self,after):
        if self.head == None:
            print("List is Empty!")
        else:
            temp = self.head
            while temp.next != None:
                if temp.data == after:
                    if temp.next.next == None:
                        self.deleteLast()
                    else:
                        temp.next,temp.next.prev = temp.next.next,temp
                    return
                temp = temp.next
            print("Element Not Found or can be the last element!")


    def deleteLast(self):
        if self.head == None:
            print("List is empty")
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.prev.next = None
        

    def printList(self):
        if self.head == None:
            print("List is Empty")
        else:
            temp = self.head
            while temp != None:
                print(temp.data,"->",end=" ")
                temp = temp.next
            print("None\n")


if __name__ == "__main__":
    l = LinkedList()
    l.insertAtBegin(2)
    l.insertAtBegin(3)
    l.insertAtBegin(4)
    l.insertAtBegin(6)
    l.printList()
    l.insertAtEnd(12)
    l.insertAfterGiven(4,5)
    l.insertBeforeGiven(2,1)
    l.printList()
    l.deleteFirst()
    l.deleteLast()
    l.printList()
    l.deleteBeforeGiven(3)
    l.printList()
    l.deleteAfterGiven(4)
    l.printList()