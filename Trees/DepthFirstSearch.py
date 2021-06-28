class Node:
    def __init__(root, val, left=None, right=None):
        root.val = val
        root.left = left
        root.right = right


'''
To make things easy for you in the next functions the only thing that is changing is the order of the print statement for the root node like

In preorder as root node is to be printed first the print statement in at start followed by left and right
Then in inorder the print state is after left but before right
And Finally in postorder the print statement is at last

Just follow the flow mentioned before each function and adjust the lines.
'''

''' Here we perfomr the PreOrder Traversal of the BST where the flow is Root-->Left-->Right'''
def preorder(root):
    # First we check if root is not None i.e. we haven't reached the end of our tree.
    if root:
        # Then we print the current element
        print(str(root.val), end = ' ')

        # Now we check if there exists a left node and if soo we call that part recursively
        if root.left:
            preorder(root.left)

        # Now we check if there exists a right node and if soo we call that part recursively
        if root.right:
            preorder(root.right)


''' Here we perfomr the InOrder Traversal of the BST where the flow is Left-->Root-->Right'''
def inorder(root):
    # First we check if root is not None i.e. we haven't reached the end of our tree.
    if root:

        # First we check if there exists a left node and if soo we call that part recursively
        if root.left:
            inorder(root.left)

        # Then we print the current element
        print(str(root.val), end = ' ')

        # Now we check if there exists a right node and if soo we call that part recursively
        if root.right:
            inorder(root.right)


''' Here we perfomr the PostOrder Traversal of the BST where the flow is Left-->Right-->Root'''
def postorder(root):
    # First we check if root is not None i.e. we haven't reached the end of our tree.
    if root:

        # First we check if there exists a left node and if soo we call that part recursively
        if root.left:
            postorder(root.left)

        # Now we check if there exists a right node and if soo we call that part recursively
        if root.right:
            postorder(root.right)
        
        # Then we print the current element
        print(str(root.val), end = ' ')


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
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print_tree(root)

    print("\n")
    print("Preorder Traversal of the tree is:")
    preorder(root)
    print("\n")

    print("Inorder Traversal of the tree is:")
    inorder(root)
    print("\n")

    print("Postorder Traversal of the tree is:")
    postorder(root)
    print("\n")