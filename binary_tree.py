class Node:
    def __init__(self, cargo, children=None):
        self.cargo = cargo
        self.children = None

    def __str__(self):
        return str(self.cargo)

root = Node(1)

root.children = Node([Node(2),Node(3)])

root.children.children = Node(4)