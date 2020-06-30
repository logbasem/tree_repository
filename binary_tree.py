class Node:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.cargo)

root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)