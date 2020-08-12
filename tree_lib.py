import treelib

from treelib import Node, Tree

tree = Tree()

tree.create_node("330",330)
tree.create_node("33",33,parent=330)
tree.create_node("10",10,parent=330)
tree.create_node("11",11,parent=33)
tree.create_node("3",3,parent=33)
tree.create_node("5",5,parent=10)
tree.create_node("2",2,parent=10)

tree.show()