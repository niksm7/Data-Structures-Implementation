class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

            
def isSymmetric(root: Node) -> bool:
    return isMirror(root, root)

# This function recursively checks if both the sides of tree have equal values.
def isMirror(t1, t2):

    # First it checks if both the sides are pointing to Null means they are equal
    if not t1 and not t2: 
        return True
    
    # If only either of them is pointing to null and other is not that means they are not equal
    if not t1 or not t2: 
        return False

    # If Null is not into play then we keep on checking equality for left and right

    # Only if current level values are same we move on to check for its child to be same
    # So we check if left.left = right.right and so on because to be symmetric mirrored image should be same.

    return t1.val == t2.val and isMirror(t1.right, t2.left) and isMirror(t1.left, t2.right)

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

    # Symmetric Tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(4)
    root.right.right = Node(3)
    print("\nTree 1\n")
    print_tree(root)

    if isSymmetric(root) == True:
        print("\nTree1 is Symmetric!\n")
    else:
        print("\nTree1 is not Symmetric!\n")


    # Asymmetric Tree
    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(2)
    root2.left.right = Node(3)
    root2.right.right = Node(3)
    print("\nTree 2\n")
    print_tree(root2)

    if isSymmetric(root2) == True:
        print("\nTree2 is Symmetric!\n")
    else:
        print("\nTree2 is not Symmetric!")

