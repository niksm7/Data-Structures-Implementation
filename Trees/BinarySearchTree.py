######################################## NODE CLASS #####################################################

class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val):
        '''For inserting the val into the tree we first start from the root node and depending on the values we either insert the val to the left or to the right'''

        ''' Now if the val of the current node is equal to the node which we want to insert then we simply reject it because duplicate values are not allowed'''

        if self.val == val:
            return False

        # Now if the val which is to be inserted is less than the current node val then we have to insert it to the left of current node

        elif self.val > val:

            # ''' If left node already exists then we recursively move down to the leaf node(last node) and then insert the node'''
            if self.left:
                return self.left.insert(val)
                
            # Now if after recursive calling or normally we have reached till the leaf node then we simply assign the new node to the left

            else:
                self.left = Node(val)
                return True

        # Now if the new node value is greater than the current node then we have to insert it to the right

        else:
            # If right node already exists then we recursively move down to the leaf node(last node) and then insert the node

            if self.right:
                return self.right.insert(val)

            # Now if after recursive calling or normally we have reached till the leaf node then we simply assign the new node to the right

            else:
                self.right = Node(val)
                return True
    

    def findMinValueNode(self,node):
        ''' As the smallest value node would be the element at the left most bottom of the tree so we move down leftwards untill the leaf node '''

        # We have created a pointer reference otherwise it will affect the root node
        current = node

        # We run the while loop untill we reach the last node on the left
        while current.left is not None:
            current = current.left
        
        # We finally return the minimum value node
        return current
    

    def findMaxValueNode(self,node):
        ''' As the larget value node would be the element at the right most bottom of the tree so we move down rightwards untill the leaf node '''

        # We have created a pointer reference otherwise it will affect the root node
        current = node

        # We run the while loop untill we reach the last node on the right
        while current.right is not None:
            current = current.right
        
        # We finally return the minimum value node
        return current
    

    def find(self,val):

        '''To find the required value node'''

        '''Logic is completely similar to the code we use to "insert" a node, just replace some points'''

        if self.val == val:
            return True
        elif self.val > val:
            if self.left:
                return self.left.find(val) 
            else:
                return False
        else:
            if self.right:
                return self.right.find(val)
            else:
                return False


    def countNodes(self,node):

        '''Count the total number of nodes in the tree'''

        if node is None:
            return 0
        return 1 + self.countNodes(node.left) + self.countNodes(node.right)


    def findHeight(self,node):

        '''Find the height of the tree which is actually the branch with maximum lenght '''

        if node is None:
            return 0
        
        return max(self.findHeight(node.left),self.findHeight(node.right))+1
    


    '''
    To make things easy for you in the next functions the only thing that is changing is the order of the print statement for the root node like

    In preorder as root node is to be printed first the print statement in at start followed by left and right
    Then in inorder the print state is after left but before right
    And Finally in postorder the print statement is at last

    Just follow the flow mentioned before each function and adjust the lines.
    '''



    ''' Here we perfomr the PreOrder Traversal of the BST where the flow is Root-->Left-->Right'''
    def preorder(self):
        # First we check if self is not None i.e. we haven't reached the end of our tree.
        if self:

            # Then we print the current element
            print(str(self.val), end = ' ')

            # Now we check if there exists a left node and if soo we call that part recursively
            if self.left:
                self.left.preorder()

            # Now we check if there exists a right node and if soo we call that part recursively
            if self.right:
                self.right.preorder()

    
    ''' Here we perfomr the InOrder Traversal of the BST where the flow is Left-->Root-->Right'''
    def inorder(self):
        # First we check if self is not None i.e. we haven't reached the end of our tree.
        if self:

            # First we check if there exists a left node and if soo we call that part recursively
            if self.left:
                self.left.inorder()

            # Then we print the current element
            print(str(self.val), end = ' ')

            # Now we check if there exists a right node and if soo we call that part recursively
            if self.right:
                self.right.inorder()
    

    ''' Here we perfomr the PostOrder Traversal of the BST where the flow is Left-->Right-->Root'''
    def postorder(self):
        # First we check if self is not None i.e. we haven't reached the end of our tree.
        if self:

            # First we check if there exists a left node and if soo we call that part recursively
            if self.left:
                self.left.postorder()

            # Now we check if there exists a right node and if soo we call that part recursively
            if self.right:
                self.right.postorder()
            
            # Then we print the current element
            print(str(self.val), end = ' ')
    
    


    

######################################## TREE CLASS #####################################################

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root == None:
            self.root = Node(val)
            return True

        else:
            return self.root.insert(val)
    
    def find(self,val):
        if self.root is not None:
            return self.root.find(val)
        else:
            return False
    
    def preorder(self):
        if self.root is not None:
            print("\nPreorder: ")
            self.root.preorder()
    
    def inorder(self):
        if self.root is not None:
            print("\nInorder: ")
            self.root.inorder()
    
    def postorder(self):
        if self.root is not None:
            print("\nPostorder: ")
            self.root.postorder()
    
    def countNodes(self):
        if self.root is not None:
            print("Total Nodes: ",self.root.countNodes(self.root))
    
    def findHeight(self):
        if self.root is not None:
            print("Height of the Tree: ",self.root.findHeight(self.root))
    
    def deleteTree(self):
        self.root = None


########### This code is taken from StackOverflow to Visually Represent the tree (NOT IMPORTANT) ############

def print_tree(root, val="val", left="left", right="right"):
    def display(root, val=val, left=left, right=right):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if getattr(root, right) is None and getattr(root, left) is None:
            line = '%s' % getattr(root, val)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if getattr(root, right) is None:
            lines, n, p, x = display(getattr(root, left))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if getattr(root, left) is None:
            lines, n, p, x = display(getattr(root, right))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = display(getattr(root, left))
        right, m, q, y = display(getattr(root, right))
        s = '%s' % getattr(root, val)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    if root is None:
        print("Tree is Empty!")
        return

    lines, *_ = display(root, val, left, right)
    for line in lines:
        print(line)


######################################## MAIN FUNCTION #####################################################


if __name__ == "__main__":

    tree = Tree()
    tree.insert(12)
    tree.insert(1)
    tree.insert(14)
    tree.insert(3)
    tree.insert(21)
    tree.insert(13)
    tree.insert(25)
    print_tree(tree.root)
    tree.preorder()
    tree.inorder()
    tree.postorder()
    print("\nElement 12 Found?",tree.find(12))
    tree.countNodes()
    tree.findHeight()
    tree.deleteTree()
    print_tree(tree.root)