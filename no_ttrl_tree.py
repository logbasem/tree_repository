"""
In this code I will be writing a simple program for a tree in python. I will not be using a tutorial this time, and will instead try to do this from
memory.
"""

class Node:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)


root = Node("Root of Tree")

root.left = Node("Left Branch")
root.right = Node("Right Branch")

root.left.left = Node("Left Left Branch")