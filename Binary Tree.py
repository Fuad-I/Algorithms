class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = None
        self.height = 1
        self.balance_factor = 0

    def __str__(self):
        return str(self.value)

    def insert(self, value):
        # Compare the new value with the parent node
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def traverse(self):
        if self:
            if self.left:
                self.left.traverse()

            if self.right:
                self.right.traverse()
            print(self.value)


class BinaryTree:
    def __init__(self, head):
        self.head = Node(head)

    def insert(self, value):
        self.head.insert(value)

    def traverse(self):
        self.head.traverse()


new_binary_tree = BinaryTree(5)
for item in [2, 8, 1, 3, 7, 9]:
    new_binary_tree.insert(item)


def traverse(node):
    current_node = node



# traverse(head)
# print(new_binary_tree.head)
new_binary_tree.traverse()
