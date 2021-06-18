class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

class Tree:
    preIndex = 0

    ''' This function may be called recursively and will help us to construct the tree'''

    def createTree(self,inOrder,preOrder,inStart,inEnd):

        if inStart > inEnd:
            return None
        
        # We get hold of the current element in the preOrder traversal by using the preIndex variable and keep on incrementing it
        curr_ele = preOrder[self.preIndex]
        self.preIndex += 1

        # Create a new node with the current element we got from preOrder
        new_node = Node(curr_ele)

        # If there are no child nodes i.e. left and right nodes to current node then we simply return the node
        if inStart == inEnd:
            return new_node
        
        # If there are child nodes present then we get the index of this current element
        inIndex = self.hash_map[curr_ele]

        # And then assign its left and right node as per the recursive call 

        # the left node will be present to the left of the current node so we pass the start index of inorder node and current node's index - 1
        new_node.left = self.createTree(inOrder,preOrder,inStart,inIndex-1)

        # The right node will be present to the right of the current node so we pass starting index as index of current node + 1 and inEnd as ending index
        new_node.right = self.createTree(inOrder,preOrder,inIndex+1,inEnd)

        # Finally we return the node that is created
        return new_node


    ''' This function is used to optimize code by using functionality of hash maps storing the indices of the elements in the inorder traversal'''

    def optimizeInformation(self,inOrder,preOrder):
        self.hash_map = {}

        # We iterate through the inorder storing the elements as key and indices as their values

        for i in range(len(inOrder)):
            self.hash_map[inOrder[i]] = i
        
        # We then return with the function to create tree which will provide the root of the tree
        return self.createTree(inOrder,preOrder,0,len(inOrder)-1)


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

if __name__ == "__main__":
    
    inOrder = [9,3,15,20,7]
    preOrder = [3,9,20,15,7]

    tree = Tree()
    root = tree.optimizeInformation(inOrder,preOrder)
    print_tree(root)