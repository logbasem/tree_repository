import treelib

from treelib import Node, Tree



def add_two_branches(tree,parent,first_value,second_value):
    tree.create_node(str(first_value),first_value,parent=parent)
    tree.create_node(str(second_value),second_value,parent=parent)

def create_tree(tier_number,top,value_list):
    binary_tree = Tree()
    binary_tree.create_node(str(top),top)

    add_two_branches(binary_tree,top,value_list[0],value_list[1])

    binary_tree.show()

tier_number = 2
top = 330
value_list = [33,10]

create_tree(tier_number,top,value_list)