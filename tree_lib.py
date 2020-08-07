import treelib

from treelib import Node, Tree

tree = Tree()

tree.create_node("150",150)
tree.create_node("15",15,parent=150)
tree.create_node("10",10,parent=150)
tree.create_node("5",5,parent=15)
tree.create_node("3",3,parent=15)
tree.create_node("5",5.2,parent=10)
tree.create_node("2",2,parent=10)

tree.show()