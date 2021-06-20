class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def displayLevelOrder(root):
    if root is None:
        return

    # We have a parent queue which we will actually contain nodes for each level
    parent_queue = [root]

    # At the same time when we are fetching out the parent nodes we will append their childs here as they
    # will make the next level

    child_queue = []

    # Counter to print each level
    level = 0
    print("\nLevel 0")

    # We run this while loop until there are nodes present in the parent queue
    while parent_queue:
        # Here we print the value which is currently at first position in the queue
        print(parent_queue[0].val)

        # We remove the first element from the parent queue as it has already been visited
        curr = parent_queue.pop(0)

        # We check if the node we removed has a left node and if so we append that node in the child queue
        if curr.left is not None:
            child_queue.append(curr.left)

        # We check if the node we removed has a right node and if so we append that node in the child queue
        if curr.right is not None:
            child_queue.append(curr.right)

        # Now if all the nodes in the parent queue are visited and the queue is now empty so we can move
        # To the next level

        if not parent_queue:
            # As the child nodes are now the parent nodes we assign the child queue to be the parent queue
            parent_queue = child_queue

            # And also make the child queue empty
            child_queue = []

            # Increase the level count and print the level
            level += 1

            # If there is something present in the parent queue only then we print the level
            if parent_queue:
                print(f"\nLevel {level}")


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
    root = Node(8)
    root.left = Node(4)
    root.right = Node(7)
    root.right.left = Node(21)
    root.right.right = Node(14)
    root.left.left = Node(9)
    root.left.right = Node(12)
    print_tree(root)
    displayLevelOrder(root)
