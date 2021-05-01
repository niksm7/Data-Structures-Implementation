class Stack():
    def __init__(self,limit=10):
        self.stack = []
        self.limit = limit
        self.length = 0
    
    def push(self,data):
        if self.length + 1 > self.limit:
            print("Stack Overflow")
        else:
            self.stack.append(data)
            self.length += 1
    
    def pop(self):
        if self.length == 0:
            print("Stack is Empty")

        else:
            x = self.stack[-1]
            self.stack = self.stack[:-1]
            self.length -= 1 
            return x
    

    def peek(self):
        if self.length == 0:
            return "Stack is Empty"
        return self.stack[-1]


    def isEmpty(self):
        return self.length <= 0

    def size(self):
        return self.length


    def printStack(self):
        print([i for i in self.stack])



if __name__ == "__main__": 
    
    n = 12  #Fixed size of our stack to check stackoverflow error
    stack1 = Stack(n)

    print("Is stack empty? - ",stack1.isEmpty())

    for i in range(n):
        stack1.push(i+1)

    print("Element Poped - ",stack1.pop())
    print("Element Poped - ",stack1.pop())


    print("Element Peeked - ",stack1.peek())

    print("Is stack empty? - ",stack1.isEmpty())

    print("Stack Size - ",stack1.size())
    

    
    stack1.printStack()


