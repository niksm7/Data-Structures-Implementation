class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def push(self,data):

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

    def pop(self):
        if self.head == None:
            print("Stack is Empty")

        temp = self.head
        prev_temp = None
        while temp.next != None:
            prev_temp = temp
            temp = temp.next
        print("Element popped",temp.data)
        if temp != self.head:
            prev_temp.next = None
        else:
            self.head = None

    def peek(self):
        if self.head == None:
            print("Stack is Empty")

        temp = self.head
        prev_temp = None
        while temp.next != None:
            prev_temp = temp
            temp = temp.next
        print("Peeked element",temp.data)
    
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
    List.push(10)
    List.push(11)
    List.pop()
    List.search(10)
    List.push(14)
    List.push(18)
    List.push(21)
    List.peek()
    List.printList()