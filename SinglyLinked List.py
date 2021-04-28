class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    
    def insertAtBegin(self,data):

        newnode = Node(data)

        if self.head == None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode

    def insertAtEnd(self,data):

        newnode = Node(data)

        if self.head == None:
            self.head = newnode

        else:
            temp = self.head

            while temp != None:
                if temp.next == None:
                    temp.next = newnode
                    break
                temp = temp.next

    def insertAtIndex(self,index,data):

        temp = self.head
        prevNode = 0
        newnode = Node(data)
        count = 0

        while temp != None:
            if count == index:
                newnode.next = prevNode.next
                prevNode.next = newnode
                return
            prevNode = temp
            temp = temp.next
            count += 1
        print("Index Range Out Of Bound")


    def delete(self,data):

        temp = self.head
        prev = 0

        if self.head.data == data:
            self.head = self.head.next
            return

        while temp != None:
            if temp.data == data:
                prev.next = temp.next
                temp.next = None
            prev = temp
            temp = temp.next

    def search(self,data):

        temp = self.head
        while temp != None:
            if temp.data == data:
                print(True)
                return
            temp = temp.next
        print(False)
    
    def printList(self):
        
        temp = self.head
        while temp != None:
            print(temp.data,end=" ")
            temp = temp.next


if __name__ == "__main__":
    List = LinkedList()
    List.head = Node(1)
    List.insertAtBegin(3)
    List.insertAtEnd(10)
    List.insertAtEnd(11)
    List.delete(10)
    List.search(3)
    List.insertAtIndex(1,21)
    List.insertAtIndex(1,10)
    List.printList()



